from socket import *
 
target_ip = input('Enter Target IP (ex:192.168.32.211) : ') # 검사할 시작 IP 주소
 
start_port = int(input('Start Port : ')) # 검사할 시작 포트 번호
end_port = int(input('Last Port : ')) # 검사할 마지막 포트 번호
 
try:
    for port in range(start_port, end_port+1):
        ipscan_sock = socket(AF_INET, SOCK_STREAM)
        ipscan_sock.settimeout(.5) # 0.5초 동안 응답이 없을 경우 종료
        result = ipscan_sock.connect_ex( (target_ip, port) )
        if result == 0:
            print('[*] Open port : \t', port)
        ipscan_sock.close()
 
except KeyboardInterrupt:  # 키보드로 'ctrl+c'로 프로그램 중지한 경우
    print('Execution canceled')
 
except gaierror:  # 호스트를 찾을 수 없는 경우
    print('Hostname could not be resolved')
 
print('Scanning completed.')
