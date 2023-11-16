# -*- coding:utf-8 -*-
# test9.py in KeyboardUC
# zhengyinloong
# 2023/11/6

import bluetooth

import time
t0 = time.time()
print(t0)
nearby_devices = bluetooth.discover_devices(lookup_names=True)
t1 = time.time()
print(t1-t0)
print(len(nearby_devices))
for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))

svs = bluetooth.find_service(uuid='0xFFF0')
