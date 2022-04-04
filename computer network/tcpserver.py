from socket import *

s_ip = 'localhost'
s_port = 9999

s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.bind((s_ip, s_port))
s_sock.listen(2)

client, c_addr = s_sock.accept()
print(c_addr, 'is connected')

data1 = 'Thx for connecting'
client.send('Thx'.encode('utf-8'))
data2 = 'Received data from client : '
print(data2, client.recv(1024).decode('utf-8'))

client.close()
s_sock.close()