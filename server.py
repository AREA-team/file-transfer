import socket

sock = socket.socket()
sock.bind(('', 9090))

while True:
    sock.listen(1)
    conn, address = sock.accept()
    print('connected:', address)
    data = conn.recv(1024)
    conn.send(data.upper())
    while data:
        data = conn.recv(1024)
        conn.send(data.upper())
