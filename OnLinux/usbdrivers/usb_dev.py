# -*- coding: UTF-8 -*-
# usb_dev.py
# Description:
# zhengyinloong
# 2023/9/2 下午1:57
# Copyright：©2020-2023 zhengyinloong

import usb.core
import usb.util




EP_IN = 0x81
EP_OUT = 0x01
dev_handle = None
kernelDriverDetached = 0


#
#  usb_dev_open.
#
def usb_dev_open(vendor_id, product_id):
    global dev_handle
    global kernelDriverDetached
    dev_handle = None
    kernelDriverDetached = 0
    if dev_handle is not None:
        usb.util.release_interface(dev_handle, 0)
    if kernelDriverDetached:
        dev_handle.attach_kernel_driver(0)
        usb.util.dispose_resources(dev_handle)
    dev_handle = None
    dev_handle = usb.core.find(idVendor=vendor_id, idProduct=product_id)
    if dev_handle is None:
        return False
    dev_handle.set_configuration()
    try:
        if dev_handle.is_kernel_driver_active(0):
            dev_handle.detach_kernel_driver(0)
            kernelDriverDetached = 1
    except NotImplementedError:
        pass
    try:
        usb.util.claim_interface(dev_handle, 0)
        return True
    except usb.core.USBError:
        return False


#
#  usb_dev_close.
#
def usb_dev_close():
    global dev_handle
    global kernelDriverDetached
    if dev_handle is not None:
        usb.util.release_interface(dev_handle, 0)
        usb.util.dispose_resources(dev_handle)
        dev_handle = None
        kernelDriverDetached = 0


#
#  usb_dev_write_sync.
#
def usb_dev_write_sync(Datas, DataLen, timeout):
    global dev_handle
    if dev_handle is None:
        return False
    ret = dev_handle.write(EP_OUT, Datas)
    if ret > 0:
        return True
        print("usb_dev_write_sync error,", ret)
    return False
#
#  usb_dev_read_sync.
#
def usb_dev_read_sync(Buf, bufsz, timeout):
    global dev_handle
    if dev_handle is None:
        return False
    data = dev_handle.read(EP_IN, bufsz, timeout=timeout)
    Buf[:] = data
    return Buf
