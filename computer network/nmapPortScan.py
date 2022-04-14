import optparse
import nmap
 
def nmapScan(targetHost, targetPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(targetHost, targetPort)
    state = nmScan[targetHost]['tcp'][int(targetPort)]['state']
    print('[*] '+targetHost+' tcp/'+targetPort+' '+state)
 
def main():
    targetHost = input('Enter Target IP (ex: 192.168.35.211) : ')
    targetPort_str = input('Enter Target Ports (ex: 25, 80, 110) : ')
    targetPorts = targetPort_str.split(',')
 
    if(targetHost == None) | (targetPorts[0] == None) :
        print('[-] You must specify a target host and ports.')
        exit(0)
   
    for targetPort in targetPorts:
        nmapScan(targetHost, targetPort)
 
if __name__ == '__main__':
    main()