import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Enter the host name: ")
port = input("Enter the port number: ")
document = input("Enter the document that you want to retrieve: ")

if len(host) < 1:
    host = "data.pr4e.org"

if len(port) < 1:
    port = 80

if len(document) < 1:
    document = "romeo.txt"

port = int(port)

my_socket.connect((host, port))

request = f'GET http://{host}/{document} HTTP/1.0\r\n\r\n'.encode()
# print(type(request))
my_socket.send(request)

while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

my_socket.close()
