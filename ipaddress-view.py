from ipaddress import *
from netaddr import *



'''ipaddress libery
    documentation:
    https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address
'''

ip1 = IPv4Interface('192.0.2.5/24')
#IPv4Network('192.0.2.0/24')

ip1.netmask
#IPv4Address('255.255.255.0')

str(ip1.netmask)
#'255.255.255.0'

ip1.ip
#IPv4Address('192.0.2.5')

ip1.network
#IPv4Network('192.0.2.0/24')

'''netaddr libery
    netaddr libery is not included as default and must be installed with pip
    Documentation:
    https://netaddr.readthedocs.io/en/latest/tutorial_01.html
'''
ip = IPNetwork('192.0.2.0/24')
ip.ip
#IPAddress('192.0.2.0')

ip.netmask
#IPAddress('255.255.255.0')

str(ip.netmask)
#'255.255.255.0'

ip.prefixlen
#24

ip.subnet
#<bound method IPNetwork.subnet of IPNetwork('192.0.2.0/24')>

ip[0]
#IPAddress('192.0.2.0')

ip[3] 
#IPAddress('192.0.2.3')
