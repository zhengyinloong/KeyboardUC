# -*- coding:utf-8 -*-
# test4.py in KeyboardUC
# zhengyinloong
# 2023/9/18
import bluetooth

# # 扫描附近的蓝牙设备，返回的是元组列表(Bluetooth地址，设备名称)
# devices = bluetooth.discover_devices(lookup_names=True,
#                                      duration=15,
#                                      flush_cache=True)
#
# for addr, name in devices:
#     print(f"Device: {addr} - {name}")

# 定义连接的地址和端口
target_address = "B0:D2:78:76:6E:21"
port = 1  # 默认端口号

# 连接到设备
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)  # 创建RFCOMM套接字对象
sock.connect((target_address, port))

# 发送消息
sock.send("Hello World")
data = sock.recv(1024)
print(f"Received: {data}")

# 关闭连接
sock.close()
