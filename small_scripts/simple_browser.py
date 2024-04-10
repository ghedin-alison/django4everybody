import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criar o telefone
# my_sock.connect(('data.pr4e.org', 80)) #ligar pra um telefone nesse ramal
my_sock.connect(('localhost', 9000)) #ligar pra um telefone nesse ramal
cmd = 'GET http://localhost/teste.txt HTTP/1.0\r\n\r\n'.encode()
my_sock.send(cmd)

while True:
    data=my_sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

my_sock.close()