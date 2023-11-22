# -*- coding:utf-8 -*-
# test_i2c.py in KeyboardUC
# zhengyinloong
# 2023/9/25

import smbus
import time
i2c_addr = 0x39
i2c_bus = smbus.SMBus(19)  # 其中 0 表示 i2c0
# i2c_bus.open(3)
tData = [0x72, 0x02, 0xff]

while True:
    for i in range(2):
        i2c_bus.write_i2c_block_data(i2c_addr, 1, tData)
        # i2c_bus.write_byte(i2c_addr,tData[i])
    print(tData)
    time.sleep(1)
