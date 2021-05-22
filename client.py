import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(b'hello, world!')

data = sock.recv(1024)
print(data)

sock.send(b'gg!')

data = sock.recv(1024)
sock.close()

print(data)