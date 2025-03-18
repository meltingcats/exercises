#!/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #INET is like IPV4 connection, socket.socktream is the port

s.connect((HOST,PORT)) #connect is socket module

#open a new connection in kali nc -nvlp 7777 to listen to that port
#then run python3 s.py on original terminal. this is lke running port scanner

