# -*- coding: utf-8 -*-

"""
A simple Python script to send messages to a sever over Bluetooth 
using PyBluez (with Python 3).
"""

import bluetooth

serverMACAddress = "98:DA:20:02:F7:57"
port = 1
mode_dict = {'w': '$1,0,0,0,0,0,0,0,0,0#',
             'a': '$3,0,0,0,0,0,0,0,0,0#',
             's': '$2,0,0,0,0,0,0,0,0,0#',
             'd': '$4,0,0,0,0,0,0,0,0,0#',
             'q': '$0,0,0,0,0,0,0,0,0,0#'}
try:
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    # HCI, L2CAP, RFCOMM, or SCO. The default is RFCOMM.
    socket.connect((serverMACAddress, port))
except OSError as e:
    print(f"{serverMACAddress} is offline", e)
    exit()

print("bluetooth connected!")

while 1:
    text = input()  # Note change to the old (Python 2) raw_input
    text = mode_dict[text]
    if text == '$0,0,0,0,0,0,0,0,0,0#':
        print("sent <" + text + "> to device:" + serverMACAddress)
        socket.send(text)
        break
    print("sent <" + text + "> to device:" + serverMACAddress)
    socket.send(text)
    data = socket.recv(1024)
    de_data = data.decode('utf-8')  # bytes -> str
    print("recv <" + de_data + "> from device:" + serverMACAddress)
    idx_1, idx_2 = 0, 0
    for i in range(len(de_data)):
        char = de_data[i]
        if char == ',':
            idx_1 = i
        if char == 'c' and i < len(de_data) - 1 and de_data[i + 1] == 'm':
            idx_2 = i
            break
    str_ultra = de_data[idx_1 + 1:idx_2]
    ultra = float(str_ultra)
    print("ultra distance ->", ultra)

socket.close()
