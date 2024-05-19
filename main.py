import ipaddress
network = ipaddress.ip_network('192.168.1.0/24')
for ip in network:
    print(ip)