from socket import AF_INET, SOCK_STREAM, SHUT_WR, socket

def create_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    try:
        server_socket.bind(('localhost', 9000))
        server_socket.listen(5)
        while(1):
            (client_socket, address) = server_socket.accept()

            rd = client_socket.recv(5000).decode()
            pieces = rd.split("\n")
            
            if(len(pieces) > 0) : print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            client_socket.sendall(data.encode())
            client_socket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting Down...\n")
    except Exception as e:
        print("Error:\n")
        print(e)

    server_socket.close()

print("Access http://localhost:9000")
create_server()