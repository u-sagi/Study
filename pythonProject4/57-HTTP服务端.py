import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 8008))

server.listen(5)

client_socket, addr = server.accept()

client_data = client_socket.recv(1024)
print(client_data.decode())

client_socket.send(b'hello')

server.close()
