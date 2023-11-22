# -*- coding:utf-8 -*-
# usbdriver.py in KeyboardUC
# zhengyinloong
# 2023/08/28 12:48
import time

import usb.core
import usb.util

import subprocess

from config.settings import *

command = 'sudo -S chmod 777 */ -R'
password = PASSWORD

process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
process.communicate(password.encode())

# sudo -S python3 usbdriver.py
def FindDevices():
    devs = usb.core.find(find_all=True)
    return devs


def FindDevice(vid, pid):
    dev = usb.core.find(idVendor=vid, idProduct=pid)  # USB\VID_0D00&PID_0721&REV_0100&MI_00
    if dev is not None:
        # print(f'{dev}')
        # print(dev)
        print('Device Found, Attempting code...')
    return dev


def ReadConfig(dev, interface_number=0, alternate_setting=0):
    if dev.is_kernel_driver_active(interface_number) is True:
        # tell the kernel to detach
        # print('tell the kernel to detach')
        dev.detach_kernel_driver(interface_number)
        # claim the device
        # print('claim the device')
        usb.util.claim_interface(dev, interface_number)
    # 获取设备的配置
    dev_config = dev.get_active_configuration()
    interface = None
    for _interface in dev_config:
        # if interface.bInterfaceClass == usb.CLASS_HID and interface.bInterfaceNumber == interface_number:
        if _interface.bInterfaceNumber == interface_number:
            # interface_number = _interface.bInterfaceNumber
            # alternate_setting = _interface.bAlternateSetting
            # interface = dev_config[(interface_number, alternate_setting)]
            interface = _interface
            break  # 找到 HID 类型的接口后退出循环

    return dev_config, interface


def Endpoints(interface):
    ep_in = None
    ep_out = None
    # print(interface)
    for ep in interface:
        if usb.util.endpoint_direction(ep.bEndpointAddress) == usb.util.ENDPOINT_IN:
            # print(ep)
            ep_in = ep
            continue
        if usb.util.endpoint_direction(ep.bEndpointAddress) == usb.util.ENDPOINT_OUT:
            # print(ep)
            ep_out = ep
            continue

    return ep_in, ep_out


def ReceiveData(device, endpoint_in):
    try:
        data = device.read(endpoint_in.bEndpointAddress,
                           endpoint_in.wMaxPacketSize,
                           timeout=endpoint_in.bInterval,
                           # timeout=10
                           )
        # print(f'1 {data}')
        return data
    except Exception as e:
        # print(e.args)
        # print(f'1 {e}')
        if e.args == ('Resource busy',):
            time.sleep(1)
        return None


def SendData(device, endpoint_out, data):
    device.write(endpoint_out.bEndpointAddress, data)


def ReleaseDevice(dev, interface_num):
    # release the device
    usb.util.release_interface(dev, interface_num)
    # # reattach the device to the OS kernel
    dev.attach_kernel_driver(interface_num)


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
    # epi = interface[0]
    # pout = interface[1]
    # print(epi)

    # ReceiveData(dev,epi)
    # data = 'hello'
    # SendData(dev, pout, data)
