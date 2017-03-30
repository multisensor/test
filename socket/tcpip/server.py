from socket import *  
from time import ctime  
  
HOST = ''  
PORT = 21567  
BUFSIZ = 1024  
ADDR = (HOST, PORT)  
  
tcpServSock = socket(AF_INET, SOCK_STREAM)  
tcpServSock.bind(ADDR)  
tcpServSock.listen(5)  
  
print('waiting for connection...')  
tcpClientSock, addr = tcpServSock.accept()  
print('...connected from: ', addr)  
  
while True:  
    data = str(tcpClientSock.recv(BUFSIZ), encoding='utf-8')  
    if not data:  
        break 
    print(data)
    tcpClientSock.send(bytes('[%s]%s'%(ctime(), data), 'utf-8'))  
  
tcpServSock.close()  

