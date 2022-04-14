from socket import *
 
net = input('Network ID (ex:192.168.32) : ') # 검사할 시작 네크워크 ID
 
start = int(input('Start host ID : ')) # 검사할 시작 호스트 ID
end = int(input('Last host ID : ')) # 검사할 마지막 호스트 ID
port = int(input('Port Number : ')) # 운용 중인지 검사할 포트 번호
 
def scan(addr):
    ipscan_sock = socket(AF_INET, SOCK_STREAM)
    setdefaulttimeout(1)
    result = ipscan_sock.connect_ex( (addr, port) )
 
    if result == 0:
        return 1
    else :
        return 0
   
    ipscan_sock.close()
 
def run():
    for ip in range(start, end+1):
        addr = net + '.' + str(ip)
        if (scan(addr)) :
            print(addr, 'is live')
 
run()
