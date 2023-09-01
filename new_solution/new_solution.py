# -*- coding:utf-8 -*-
# new_solution.py in KeyboardUC
# zhengyinloong
# 2023/09/01 10:07

import usb.core
import usb.util
import sys
import threading
import time

VID = 0x25A7
PID = 0xFA23
dev = usb.core.find(idVendor=VID, idProduct=PID)
cfg = dev.get_active_configuration()
intf = cfg[(0, 0)]

print(intf)

write_ep = usb.util.find_descriptor(
    intf,
    custom_match= \
        lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == \
            usb.util.ENDPOINT_OUT
)

read_ep = usb.util.find_descriptor(
    intf,
    custom_match= \
        lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == \
            usb.util.ENDPOINT_IN
)


def write_endpoint_thread():
    while True:
        try:
            write_ep.write("0123456789")
        except:
            print("write error")


def read_endpoint_thread():
    while True:
        try:
            data = read_ep.read(64)
            size = len(data)
            if size > 0:
                print("recv %d bytes:" % size, end='')
                for i in range(0, size):
                    print("%c" % data[i], end='')
                print('')
        except Exception as e:
            print("no data")
            print(e)


def main():
    r = threading.Thread(target=read_endpoint_thread)
    # w = threading.Thread(target=write_endpoint_thread)
    r.start()
    # w.start()
    r.join()
    # w.join()
    dev.reset()


if __name__ == '__main__':
    main()

