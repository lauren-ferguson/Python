# IP Gen w/Subnet Input
# Input Subnet 1
subnet = 0
while not int(subnet) in range(1, 36):
    subnet = input("Please enter your subnet (1 - 35) : ")  # choose a subnet
    
# IP Gen 1
import random

for i in range(1):
    print(".".join(str(random.randint(0, 255)) for _ in range(4)) + "/" + subnet)

    
# Subnet 2
subnet2 = 0
while not int(subnet2) in range(1, 36):
    subnet2 = input("Pick another subnet (1 - 35) : ")  # choose a subnet

# IP Gen 2
for i in range(1):
    print(".".join(str(random.randint(0, 255)) for _ in range(4)) + "/" + subnet2)

