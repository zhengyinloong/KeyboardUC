# -*- coding: UTF-8 -*-
# main.py
# Description:
# zhengyinloong
# 2023/9/2 下午2:08
# Copyright：©2020-2023 zhengyinloong

import usb_dev
import subprocess

command = 'sudo -S python3 main.py'
password = '123456'

process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
process.communicate(password.encode())

if __name__ == "__main__":





    # Open USB device with VID=0x1234 and PID=0x1001
    if not usb_dev.usb_dev_open(0x25A7, 0xFA23):
        print("usb_dev_open fail!")
        exit(-1)
    print("usb_dev_open ok")
    TxBuff = bytearray(512)  # 端点最大数据为512字节
    RxBuff = bytearray(512)
    usb_dev.usb_dev_write_sync(TxBuff, 512, 1000)  # 超时1000ms
    usb_dev.usb_dev_read_sync(RxBuff, 512, 1000)  # 超时1000ms
    print("RxBuff:", RxBuff)
    usb_dev.usb_dev_close()
