import optparse
import nmap
 
def nmapScan(targetHost, targetPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(targetHost, targetPort)
    state = nmScan[targetHost]['tcp'][int(targetPort)]['state']
    print('[*] '+targetHost+' tcp/'+targetPort+' '+state)
 
def main():
    parser = optparse.OptionParser('usage %prog -H <tgt_host> -P <tgt_port>') # 옵션 사용을 위한 파서 생서, 사용법에 대한 안내문을 옵션으로 제공
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host') # -H 옵션과 그 옵션값을 tgtHost에 저장하도록 옵션 추가
    parser.add_option('-P', dest='tgtPort', type='string', help='ports separated by comma') # -P 옵션과 그 옵션값을 tgtPort에 저장하도록 옵션 추가
 
    # 커맨드 라인에서 입력한 옵션 값을 options에 저장
    (options, args) = parser.parse_args() # 파싱된 옵션값을 저장
    targetHost = options.tgtHost # 옵션값에서 호스트 IP 저장
 
    # 옵션값에서 쉼표로 구분하여 포트 저장
    targetPorts = str(options.tgtPort).split(',')
   
    if(targetHost == None) | (targetPorts[0] == None) :
        print('[-] You must specify a target host and ports.')
        exit(0)
   
    for targetPort in targetPorts:
        nmapScan(targetHost, targetPort)
 
if __name__ == '__main__':
    main()