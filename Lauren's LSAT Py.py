'''
1. Which of the following could be the order in which the
friends graduated?
(A) P, M, N, R, K, L, O
(B) P, M, L, N, K, R, O
(C) P, K, N, O, L, M, R
(D) M, P, N, K, L, O, R
(E) P, M, N, O, L, K, R

2. Which of the following must be false?
(A) L graduates one year before O.
(B) M graduates one year before N.
(C) R graduates one year before O.
(D) R graduates one year before K.
(E) R graduates one year before N.

'''

# Include each name value in a list 
names = ['P', 'M', 'N', 'O', 'L', 'K', 'R']

# Use permutations function from itertools library to create a list of all possible scenarios
from itertools import permutations 

# Create a list of each possible combination of all 7 values
possible_combinations = list(permutations(names, 7))

# Eliminate scenarios based on rules

# Rule 1 - K graduated two years before O.

# We use a for loop because we are working with a list and want this to repeat a fixed number of times
# A for loop is always paired with an iterable object (i.e. list, range)
# .copy command copies metadata of the source
# use range because range of values
# use len command to return number of items in object
for scenario in possible_combinations.copy():
    for x in range(0, len(scenario)):
        if scenario[x] == 'K':
            index_of_k = x
        elif scenario[x] == 'O':
            index_of_o = x
    if index_of_k == index_of_o - 2:
        pass
    else:
        possible_combinations.remove(scenario)


# Rule 2 - P and M graduated in consecutive years, though not necessarily in that order.
for scenario in possible_combinations.copy():
    for x in range(0, len(scenario)):
        if scenario[x] == 'P':
            index_of_p = x
        if scenario[x] == 'M':
            index_of_m = x
# use abs command to return absolute value
    if abs(index_of_p - index_of_m) == 1:
        pass
    else:
        possible_combinations.remove(scenario)

# Rule 3 - N graduated third

# run simple for loop because not working with a range
for scenario in possible_combinations.copy():
    if scenario[2] == 'N':
        pass
    else:
        possible_combinations.remove(scenario)


# Rule 4 - L did not graduate sixth

for scenario in possible_combinations.copy():
    if scenario[5] == 'L':
        possible_combinations.remove(scenario)

'''1. Which of the following could be the order in which the
friends graduated?
(A) P, M, N, R, K, L, O
(B) P, M, L, N, K, R, O
(C) P, K, N, O, L, M, R
(D) M, P, N, K, L, O, R
(E) P, M, N, O, L, K, R'''
print('\nQuestion 1:')
for scenario in possible_combinations.copy():
    if list(scenario) == ['P', 'M', 'N', 'R', 'K', 'L', 'O']:
        print("Answer is A")
    if list(scenario) == ['P', 'M', 'L', 'N', 'K', 'R', 'O']:
        print("Answer is B")
    if list(scenario) == ['P', 'K', 'N', 'O', 'L', 'M', 'R']:
        print("Answer is C")
    if list(scenario) == ['M', 'P', 'N', 'K', 'L', 'O', 'R']:
        print("Answer is D")
    if list(scenario) == ['P', 'M', 'N', 'O', 'L', 'K', 'R']:
        print("Answer is E")
'''2. Which of the following must be false?
(A) L graduates one year before O.
(B) M graduates one year before N.
(C) R graduates one year before O.
(D) R graduates one year before K.
(E) R graduates one year before N.'''
# use false command to eliminate scenarios
ansA = False
ansB = False
ansC = False
ansD = False
ansE = False
print('\nQuestion 2')
# use indexes here to search for given instance of scenario
for scenario in possible_combinations.copy():
    indexes = {}
    for x in range(0, len(scenario)):
        indexes[scenario[x]] = x
    if scenario[indexes['O'] -1] == 'L':
        ansA = True
    if scenario[indexes ['N'] -1] == 'M':
        ansB = True
    if scenario[indexes ['O'] -1] == 'R':
        ansC = True
    if scenario[indexes ['K'] -1] == 'R':
        ansD = True
    if scenario[indexes ['N'] -1] == 'R':
        ansE = True
# now we address all the false commands
if not ansA:
    print("Answer is A")
elif not ansB:
    print("Answer is B")
elif not ansC:
    print("Answer is C")
elif not ansD:
    print("Answer is D")
elif not ansE:
    print("Answer is E")

