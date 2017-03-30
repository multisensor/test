#!/usr/bin/env python

from socket import *

HOST = "localhost"
PORT = 21567
BUFSIZE = 1024

ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("waiting for input message...\n")
    if not data:
        break
    udpCliSock.sendto(bytes(data, "utf-8"), ADDR)
    data, addr = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print("client recvived:", data, "from", addr)

udpCliSock.close()
