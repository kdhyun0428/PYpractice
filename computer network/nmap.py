# nmap 설치 : pip install python-nmap
import nmap
 
targetHost = '192.168.35.211'
nmScan = nmap.PortScanner()
nm = nmScan.scan(targetHost, '22-80')
 
print(nm);print()
print(nm['nmap']);print()
print(nm['scan']);print()
print(nm['scan']['192.168.35.211']);print()
print(nm['scan']['192.168.35.211']['status']);print()
print(nm['scan']['192.168.35.211']['addresses']);print()