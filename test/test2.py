# -*- coding:utf-8 -*-
# test2.py in KeyboardUC
# zhengyinloong
# 2023/08/30 15:55
import time

import usb.core
import usb.util

# 定义相关的常量
VENDOR_ID = 0x0D00  # 替换为你的设备的供应商ID
PRODUCT_ID = 0x0721  # 替换为你的设备的产品ID

# 查找设备
dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
name = usb.util.get_string(dev, 2)  # 假设字符串描述符索引为 4
print(name)
# 判断设备是否找到
if dev is None:
    raise ValueError("设备未找到")
#
# # 获取设备的配置
dev_config = dev.get_active_configuration()
interface_number = 0  # 接口索引号
alternate_setting = 0  # 备用设置索引号

for interface in dev_config:
    if interface.bInterfaceClass == usb.CLASS_HID:
        interface_number = interface.bInterfaceNumber
        alternate_setting = interface.bAlternateSetting
        break  # 找到 HID 类型的接口后退出循环
interface = dev_config[(interface_number, alternate_setting)]
print(interface)

# 进行设备配置
dev.set_configuration()

# 寻找 HID 接口和端点

# 打开设备
ep_in = None
for ep in interface:
    if usb.util.endpoint_direction(ep.bEndpointAddress) == usb.util.ENDPOINT_IN:
        # print(ep)
        ep_in = ep
        break

if ep_in is None:
    raise ValueError("未找到 IN 类型的端点")

delay = ep_in.bInterval / 1000
data = b''

# while True:
#     try:
#         time.sleep(delay)
#
#         data = ep_in.read(1000)
#         break
#     except Exception as e:
#         print(e)

# 关闭设备
usb.util.dispose_resources(dev)

