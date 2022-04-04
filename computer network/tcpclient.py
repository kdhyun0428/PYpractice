from socket import *

s_ip = 'local_host'
s_port = 9999

c_sock = socket(AF_INET, SOCK_STREAM)
c_sock.connect((s_ip, s_port))

data1 = 'Received data from server : '
print('Received from server : ',c_sock.recv(1024).decode('utf-8'))
data2 = 'Hello TCP server.'
c_sock.send(data2.encode('utf-8'))

c_sock.close()