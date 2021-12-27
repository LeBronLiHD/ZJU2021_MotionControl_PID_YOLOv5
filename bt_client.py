# -*- coding: utf-8 -*-

"""
A simple Python script to send messages to a sever over Bluetooth 
using PyBluez (with Python 3).
"""

import bluetooth

serverMACAddress = '28:54:71:26:12:96'
port = 3
socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("bluetooth connecting ...")
socket.connect((serverMACAddress, port))

while 1:
    text = input() # Note change to the old (Python 2) raw_input
    if text == "quit":
    	break
    print("sent <" + text + "> to device:" + serverMACAddress)
    socket.send(text)

socket.close()
