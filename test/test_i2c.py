# -*- coding:utf-8 -*-
# test_i2c.py in KeyboardUC
# zhengyinloong
# 2023/9/25

import serial

# I2C_test.py

# -*- coding:utf-8 -*-

import smbus
import time

i2c_addr = 0x72
i2c_bus = smbus.SMBus(0)  # 其中 0 表示 i2c0
tData = [0x02, 0xff,3]

while True:
    for i in range(2):
        i2c_bus.write_byte_data(i2c_addr,0x02,tData[i])
    print(tData)
    time.sleep(1)
