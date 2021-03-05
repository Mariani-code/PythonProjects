from itertools import permutations
perm = permutations([i for i in range(0,10)], 10)
perm = sorted(perm)
number_mil = ''
for i in perm[1000000-1]:
    number_mil  += str(i)
print(number_mil)
