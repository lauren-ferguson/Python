# RANDOM IP GENERATOR BASED ON CIDR INPUT
# import packages
import ipaddress
import random

# generate 2 random ips with subnet
name: str = input("Your name ")
for i in range(2):
    print(name, "your IP random generation is " + str(ipaddress.ip_network(random.randint(0,2 ** 32))))