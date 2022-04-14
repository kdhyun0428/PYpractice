from socket import *
 
target_ip = '192.168.35.211'     # 검사할 IP주소
target_port = 139                # 검사할 포트번호
 
ipscan_sock = socket(AF_INET, SOCK_STREAM)
 
result = ipscan_sock.connect_ex( (target_ip, target_port) )
 
if result == 0:
    print(target_ip, 'is alive')
 
ipscan_sock.close()