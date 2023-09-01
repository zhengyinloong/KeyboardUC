# -*- coding:utf-8 -*-
# main.py in KeyboardUC
# zhengyinloong
# 2023/08/31 23:36

import hid
devices = hid.enumerate()

# for device in devices:
#     print(device)
VENDOR_ID = 1739
PRODUCT_ID = 52632
device = hid.device()
device.open(VENDOR_ID, PRODUCT_ID)  # 替换成您的设备的厂商ID和产品ID
print(device.get_indexed_string(25))
command = 0x00  # 示例命令
ans = device.write(command)
print(ans)

# received_data = device.read(64)  # 读取最多64个字节的数据

