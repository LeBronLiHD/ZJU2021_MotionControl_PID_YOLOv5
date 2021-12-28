# -*- coding: utf-8 -*-

"""
A simple Python script to send messages to a sever over Bluetooth 
using PyBluez (with Python 3).
"""

import bluetooth

serverMACAddress = "98:DA:20:02:F7:57"
port = 1
try:
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    # HCI, L2CAP, RFCOMM, or SCO. The default is RFCOMM.
    socket.connect((serverMACAddress, port))
except OSError as e:
    print(f"{serverMACAddress} is offline", e)
    exit()

while 1:
    text = input()  # Note change to the old (Python 2) raw_input
    if text == '$0,0,0,0,0,0,0,0,0,0#':
        print("sent <" + text + "> to device:" + serverMACAddress)
        socket.send(text)
    	break
    print("sent <" + text + "> to device:" + serverMACAddress)
    socket.send(text)

socket.close()
