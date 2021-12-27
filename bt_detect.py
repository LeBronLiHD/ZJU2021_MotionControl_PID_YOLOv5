# -*- coding: utf-8 -*-

import bluetooth

target_name = "Tuan Earphone"
target_address = "28:54:71:26:12:96"

nearby_devices = bluetooth.discover_devices()

for bd_addr in nearby_devices:
    if target_name == bluetooth.lookup_name(bd_addr):
        target_address = bd_addr
        break

if target_address is not None:
    print("Found target with address ->", target_address)
else:
    print("Can not find device nearby!")
