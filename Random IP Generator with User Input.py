# RANDOM IP GENERATOR BASED ON CIDR INPUT
# import packages
import ipaddress
import random

# generate random
name: str = input("Your name ") # name input
for i in range(2): # output 2 random IPs
    print(name, "your IP random generation is " + str(ipaddress.ip_network(random.randint(0,2 ** 32)))) # print input name and IPs
