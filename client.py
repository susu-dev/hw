from socket import *

def send(sock):
    sendData = input('>>> ')
    sock.send(sendData.encode('utf-8'))

def recv(sock):
    recvData = sock.recv(1024)
    print('recieved : ', recvData.decode('utf-8'))

port = 8080

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('127.0.0.1', port))

print('Connection Success')

while True:
    recv(clientSocket)
    send(clientSocket)

# ---Second---
# port = 8080
#
# clientSocket = socket(AF_INET, SOCK_STREAM)
# clientSocket.connect(('127.0.0.1', port))   # 클라이언트에서 서버에 접속
#                                             # 127.0.0.1 : client
#                                             # 8080 : server port #
# print('Connection Success')
#
# while True:
#     recvData = clientSocket.recv(1024)
#     print('recieved data :', recvData.decode('utf-8'))
#
#     sendData = input('>>> ')
#     clientSocket.send(sendData.encode(('utf-8')))


# ---Init---
# clientSocket.send('I am a client'.encode('utf-8'))
#
# print('Send message')
#
# data = clientSocket.recv(1024)
# print('recieved data : ',data.decode('utf-8'))

                                       
