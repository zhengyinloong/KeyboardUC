# -*- coding: UTF-8 -*-
# bluetoothdriver.py
# Description:
# zhengyinloong
# 2023/9/3 上午10:19
# Copyright：©2020-2023 zhengyinloong

import bluetooth


def FindDevices():
    # # 扫描附近的蓝牙设备
    devices = bluetooth.discover_devices(duration=15, lookup_names=True)
    return devices

def ConnectDevice(device_address):
    # 选择要连接的蓝牙设备
    # device_address = "14:DD:9C:BC:51:7C"  # 根据实际情况填写
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    # 连接到蓝牙设备的端口
    port = 1  # 这是 RFCOMM 端口的默认值
    sock.connect((device_address, port))

    return sock


# # 发送数据
# data = "Hello, Bluetooth!"
# sock.send(data)

# # 接收数据
# received_data = sock.recv(1024)
# print("接收到的数据:", received_data)

# # 断开连接
# sock.close()
if __name__ == '__main__':
    device_address = 'C0:00:A5:B5:00:03'
    ConnectDevice(device_address)
