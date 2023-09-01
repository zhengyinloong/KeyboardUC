# -*- coding:utf-8 -*-
# main.py in KeyboardUC
# zhengyinloong
# 2023/08/31 23:09

import serial
from time import sleep
from defserial import *

if __name__ == '__main__':
    print(serial.tools.list_ports.comports())
    serial = serial.Serial('COM1', 9600, timeout=0.5)
    if serial.isOpen():
        print("open success")
    else:
        print("open failed")

    # 这里如果不加上一个while True，程序执行一次就自动跳出了
    while True:
        a = input("输入要发送的数据：")
        send(serial, a)
        sleep(0.5)  # 起到一个延时的效果
        data = recv(serial)
        if data != '':
            print("receive : ", data)
