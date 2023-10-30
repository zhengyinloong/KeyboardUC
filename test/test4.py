# -*- coding:utf-8 -*-
# test4.py in KeyboardUC
# zhengyinloong
# 2023/9/18
import bluetooth

# 寻找蓝牙设备
devices = bluetooth.discover_devices()

# 打印找到的设备列表
for device in devices:
    print(device)

# 连接到设备
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((device, 1))

# 发送数据
data = "Hello, Bluetooth!"
sock.send(data)

# 接收数据
received_data = sock.recv(1024)
print("Received: {}".format(received_data))

# 断开连接
sock.close()
