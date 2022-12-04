# IP Gen w/Subnet Input
# Input Subnet
shift = 0
while not int(shift) in range(1, 36):
    shift = input("Please enter your subnet (1 - 35) : ")  # choose a subnet
    
# IP Gen, 2 Outputs
import random
for i in range(2):
    print(".".join(str(random.randint(0, 255)) for _ in range(4)) + "/" + shift)
