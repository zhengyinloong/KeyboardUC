# -*- coding:utf-8 -*-
# usbdriver.py in KeyboardUC
# zhengyinloong
# 2023/08/28 12:48
import time

import usb.core
import usb.util


def FindDevices():
    devs = usb.core.find(find_all=True)
    return devs


def FindDevice(vid, pid):
    dev = usb.core.find(idVendor=vid, idProduct=pid)  # USB\VID_0D00&PID_0721&REV_0100&MI_00
    # if dev != None:
    #     dev.set_configuration()
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
        data = device.read(endpoint_in.bEndpointAddress, 64)
        print(f'{data}')
        time.sleep(endpoint_in.bInterval / 1000)
        # if data == b'\x01':
        data = device.read(endpoint_in.bEndpointAddress, 7)
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
    # name = usb.util.get_string(dev, 0)
    # print(name, '\n', dev)
    interface = ReadConfig(dev)[1]
    print(interface)
    epin = interface[0]
    epout = interface[1]
    # print(epin)

    # ReceiveData(dev,epin)
    # data = 'hello'
    # SendData(dev, epout, data)
