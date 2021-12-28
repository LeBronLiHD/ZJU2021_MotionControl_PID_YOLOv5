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
server_port = 1  # default
ultra_distance = -1

try:
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    # HCI, L2CAP, RFCOMM, or SCO. The default is RFCOMM.
    socket.connect((server_address, server_port))
except OSError as e:
    print(f"{server_address} is offline", e)
    exit()

print("bluetooth connected!")
mode_dict = {'w': '$1,0,0,0,0,0,0,0,0,0#',
             'a': '$3,0,0,0,0,0,0,0,0,0#',
             's': '$2,0,0,0,0,0,0,0,0,0#',
             'd': '$4,0,0,0,0,0,0,0,0,0#',
             'q': '$0,0,0,0,0,0,0,0,0,0#'}


def quit_connection():
    print("bluetooth closed.")
    socket.close()


def read_ultra():
    return ultra_distance


def refresh_ultra(data):
    de_data = data.decode('utf-8')  # bytes -> str
    print("recv <" + de_data + "> from device:" + server_address)
    idx_1, idx_2 = 0, 0
    for i in range(len(de_data)):
        char = de_data[i]
        if char == ',':
            idx_1 = i
        if char == 'c' and i < len(de_data) - 1 and de_data[i + 1] == 'm':
            idx_2 = i
            break
    str_ultra = de_data[idx_1 + 1:idx_2]
    ultra_distance = float(str_ultra)
    print("ultra distance ->", ultra_distance)


def control(mode=None):
    text = mode_dict[mode]
    socket.send(text)
    data = socket.recv(1024)
    refresh_ultra(data)


def run_test():
    control(mode='w')
    time.sleep(0.5)
    control(mode='s')
    time.sleep(0.5)
    control(mode='a')
    time.sleep(2)
    control(mode='d')
    time.sleep(2)
    control(mode='q')
    quit_connection()


if __name__ == "__main__":
    run_test()
