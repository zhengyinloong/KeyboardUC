# -*- coding:utf-8 -*-
# test_i2c.py in KeyboardUC
# zhengyinloong
# 2023/9/25

import serial

ser = serial.Serial(port="/dev/ch34x_pis1",
                    baudrate=19200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_TWO,
                    bytesize=serial.EIGHTBITS,
                    timeout=0.500,
                    )
ser.flushInput()
ser.flushOutput()
ser.write(bytearray([0x02, 0xff]))
test = ser.read()
