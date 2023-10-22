# -*- coding:utf-8 -*-
# test6.py in KeyboardUC
# zhengyinloong
# 2023/10/17

r = 0
c = 0
keycode = 4
data_str = f'12 {r:02x} {c:02x} {keycode:02x}'
data = bytes.fromhex(data_str).ljust(8, b'\xff')

print(data)
