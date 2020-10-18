# CalculatingIPAddressesWithPython
Examples from two good liberies that can help finding hostmask, prefixlength and such in python

Example of for-loop of addresses:

ip2 = IPNetwork('192.168.0.0/29')
>>> for addresses in ip2:
...     print(addresses)  
... 
192.168.0.0
192.168.0.1
192.168.0.2
192.168.0.3
192.168.0.4
192.168.0.5
192.168.0.6
192.168.0.7


ip2 = IPNetwork('192.168.0.100/29')
>>> for addresses in ip2:
...     print(addresses)        
... 
192.168.0.96
192.168.0.97
192.168.0.98
192.168.0.99
192.168.0.100
192.168.0.101
192.168.0.102
192.168.0.103
