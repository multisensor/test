#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from socket import *
from time import ctime

HOST = "127.0.0.1"
PORT = 21567
BUFSIZE = 1024

ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("waiting for message...\n")
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    if not data:
        print("client has exist")
        break
    print("server recvived:", data, "from", addr)
    udpSerSock.sendto(bytes('[%s] %s'%(ctime(),data), "utf-8"),addr) 

udpSerSock.close()
