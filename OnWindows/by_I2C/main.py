# -*- coding:utf-8 -*-
# main.py in KeyboardUC
# zhengyinloong
# 2023/08/31 23:36


import smbus2 as smbus

# 创建一个I2C对象，指定总线号
i2c_bus = smbus.SMBus(1)  # 根据实际情况选择总线号，通常为0或1

DEVICE_ADDRESS = 0x04  # I2C设备地址，根据实际情况进行更改

# 读取数据
def read_data():
    data = i2c_bus.read_byte(DEVICE_ADDRESS)
    return data

# 写入数据
def write_data(data):
    i2c_bus.write_byte(DEVICE_ADDRESS, data)

# 在这里可以添加其他I2C通信相关的函数

# 示例：从设备中读取数据并打印
data = read_data()
print("Data read from device:", data)

# 示例：向设备写入数据
write_data(0x55)
print("Data written to device.")

# 在使用完毕后，记得关闭I2C连接
i2c_bus.close()

