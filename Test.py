import ipaddress

net = ipaddress.ip_network('ip/mask', strict=False)

for ip in net.hosts():
    print(ip)