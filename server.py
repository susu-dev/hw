from socket import *

def send(sock):
    sendData = input('>>> ')
    sock.send(sendData.encode('utf-8'))

def recv(sock):
    recvData = sock.recv(1024)
    print('recieved : ', recvData.decode('utf-8'))

port = 8080

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', port))
serverSocket.listen(1)

print('Waiting Conncection port #%d' %port)

connSocket, addr = serverSocket.accept()

print('Connected at addr #', str(addr))

while True:
    send(connSocket)
    recv(connSocket)

# # 서버 socket 생성 = 인자(Address Family(주소체계), 소켓 타입)
# serverSocket = socket(AF_INET, SOCK_STREAM) # AF_INET : IPv4
#                                             # SOCKET_STREAM : 연결을 위한 스트림 소켓
#                                             # SOCKET_DGRAM : 연결되지 않은 데이터 보고용 소켓
# serverSocket.bind(('', port))   # socket bind((ip, port)) : 생성된 소켓의 번호와 실제 AF 연결
#                                 # ip -> '' : INADDR_ANY 모든 인터페이스와 연결
#                                 # port 8080 에서 모든 인터페이스에게 연결
# serverSocket.listen(1)  # listen(#) : 동시접속 수
#
# print('Waiting Connection port \'%d\'...' %port)
#
# #--- 서버 소켓은 상대방의 접속이 올 때까지 계속 대기하는 상태 ---
#
# connSocket, addr = serverSocket.accept()    # 접속 수락, 통신
#                                             # return 새로운 소켓, 상대방의 AF
# print('Connected at ', str(addr))
#
# while True:
#     sendData = input('>>> ')
#     connSocket.send(sendData.encode('utf-8'))
#
#     recvData = connSocket.recv(1024)
#     print('recieved data : ', recvData.decode('utf-8'))
