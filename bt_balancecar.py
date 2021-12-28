# -*- coding: utf-8 -*-

"""
control the balance car through bluetooth
前0x01
后0x02
左0x04
右0x03
停0x07
"""

import bluetooth
import time
import math
import numpy

server_address = "98:DA:20:02:F7:57"
server_port = 4  # default

try:
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    # HCI, L2CAP, RFCOMM, or SCO. The default is RFCOMM.
    socket.connect((server_address, server_port))
except OSError as e:
    print(f"{server_address} is offline", e)
    exit()

mode_dict = {'w':'$1,0,0,0,0,0,0,0,0,0#',
             'a':'$3,0,0,0,0,0,0,0,0,0#',
             's':'$2,0,0,0,0,0,0,0,0,0#',
             'd':'$4,0,0,0,0,0,0,0,0,0#',
             'q':'$0,0,0,0,0,0,0,0,0,0#'}


def control(mode=None):
    text = mode_dict[mode]
    socket.send(text)
    if mode == 'q':
        print("socket closd")
        socket.close()


def run_test():
    control(mode='w')
    time.sleep(0.5)
    control(mode='s')
    time.sleep(0.5)
    control(mode='a')
    time.sleep(0.5)
    control(mode='d')
    time.sleep(0.5)
    control(mode='q')


if __name__ == "__main__":
    run_test()
