# -*- coding:utf-8 -*-
# usbdriver.py in KeyboardUC
# zhengyinloong
# 2023/08/28 12:48

import os

os.environ['PYUSB_DEBUG'] = 'debug'

import time

import usb.core
import usb.util
import libusb
import subprocess

from config.settings import *

command = 'sudo -S chmod 777 */ -R'
password = PASSWORD

process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
process.communicate(password.encode())


# sudo -S python3 usbdriver.py
def FindDevices():
    devs = usb.core.find(find_all=True)
    # devs = libusb.open_device_with_vid_pid()
    return devs


def FindDevice(vid, pid):
    dev = usb.core.find(idVendor=vid, idProduct=pid)  # USB\VID_0D00&PID_0721&REV_0100&MI_00
    if dev is not None:
        # dev.set_configuration()
        # if dev.is_kernel_driver_active(0):
        #     print('detach kernel driver')
        #     dev.detach_kernel_driver(0)
        dev.reset()
    # clear any junk in the read buffer - so that init cmds will send
    return dev


def ReadConfig(dev, interface_number=0, alternate_setting=0):
    # 获取设备的配置
    dev_config = dev.get_active_configuration()

    for interface in dev_config:
        # if interface.bInterfaceClass == usb.CLASS_HID and interface.bInterfaceNumber == interface_number:
        if interface.bInterfaceNumber == interface_number:
            # interface_number = interface.bInterfaceNumber
            alternate_setting = interface.bAlternateSetting
            break  # 找到 HID 类型的接口后退出循环
    interface = dev_config[(interface_number, alternate_setting)]
    return dev_config, interface


def Endpoints(interface):
    ep_in = None
    ep_out = None
    for ep in interface:
        if usb.util.endpoint_direction(ep.bEndpointAddress) == usb.util.ENDPOINT_IN:
            # print(ep)
            ep_in = ep
        if usb.util.endpoint_direction(ep.bEndpointAddress) == usb.util.ENDPOINT_OUT:
            # print(ep)
            ep_out = ep

    return ep_in, ep_out


def ReceiveData(device, endpoint_in):
    # print(epin.bInterval)
    try:
        print(f'trying receive data from endpoint {endpoint_in.bEndpointAddress}')
        data = device.read(endpoint_in.bEndpointAddress, 64,5000)
        print(f'{data}')
        time.sleep(endpoint_in.bInterval / 1000)
        # if data == b'\x01':
        # data = device.read(endpoint_in.bEndpointAddress, 7)
        return data
        # else:
        #     return data
        # return None
    except Exception as e:
        print(e)
        return None


def SendData(device, endpoint_out, data):
    data = data.encode()
    device.write(endpoint_out.bEndpointAddress, data)


if __name__ == '__main__':
    # dev = FindDevice(vid=0x0D00, pid=0x0721)
    # devs = FindDevices()
    # print(devs)
    # for dev in devs:
    #     print(dev)
    dev = FindDevice(vid=0x25a7, pid=0xfa23)
    print(dev)
    name = usb.util.get_string(dev, 0)
    # print(name, '\n', dev)
    # interface = ReadConfig(dev)[0]
    # print(interface)
    # epin = interface[0]
    # epout = interface[1]
    # print(epin)

    # ReceiveData(dev,epin)
    # data = 'hello'
    # SendData(dev, epout, data)
