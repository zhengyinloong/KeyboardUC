# -*- coding:utf-8 -*-
# test3.py in KeyboardUC
# zhengyinloong
# 2023/08/30 23:45
import time

import hid

for device_dict in hid.enumerate():
    keys = list(device_dict.keys())
    keys.sort()
    for key in keys:
        print("%s : %s" % (key, device_dict[key]))
    print()
try:
    print("Opening the device")

    h = hid.device()
    h.open(0x0d00, 0x0721)  # TREZOR VendorID/ProductID

    device = hid.HidDeviceFilter(vendor_id=0x0d00, product_id=0x0721).get_devices()
except:
    pass
