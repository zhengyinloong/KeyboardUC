# -*- coding:utf-8 -*-
# defserial.py in KeyboardUC
# zhengyinloong
# 2023/08/31 23:09

from time import sleep


def recv(serial):
    while True:
        data = serial.read_all().hex()
        if data == '':
            continue
        else:
            break
        sleep(0.02)
    return data


def send(serial, send_data):
    send_data_hex = bytes.fromhex(send_data)
    if (serial.isOpen()):
        serial.write(send_data_hex)  # 编码
        print("发送成功", send_data_hex)
    else:
        print("发送失败！")
