# RANDOM IP GENERATOR
import random
for i in range(2):
    print(".".join(str(random.randint(0,255)) for _ in range(4)))

