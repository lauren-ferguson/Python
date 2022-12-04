# RANDOM IP GENERATOR BASED ON CIDR INPUT
# import packages
import ipaddress
import random

# generate 2 random ips with subnet
for i in range(2):
    print(str(ipaddress.ip_network(random.randint(0,2 ** 32))))