import socket
import threading


bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip,bind_port))

def handle_get(client):
    req = client.recv(1024)
    print(f'RECEIVED: {req}')
    client.send(b'ACK!')    
    client.close()

while True:
    client, addr = server.accept()
    print(f'We were accepting connections of:{addr[0]}:{addr[1]}')
    client_worker = threading.Thread(target=handle_get, args=(client,))
    client_worker.start()