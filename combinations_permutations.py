from itertools import permutations, combinations, combinations_with_replacement

lst = [1, 2, 3]
# perm = permutations(lst)
perm = permutations(lst, 2)

for i in list(perm):
    print(i)


print('\n\n')


comb = combinations(lst, 2)

for i in list(comb):
    print(i)


print('\n\n')


comb = combinations_with_replacement(lst, 2)

for i in list(comb):
    print(i)
