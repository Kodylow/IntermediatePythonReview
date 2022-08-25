# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b, repeat=2) # cartesian product
print(list(prod))

from itertools import permutations
a = [1,2,3]
perm = permutations(a, 2) # length arg, will have repetitions
print(list(perm))

from itertools import combinations, combinations_with_replacement
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a,2) #elements with themselves

from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a) # default computes sums
print(list(acc))
acc = accumulate(a, func=max)


from itertools import groupby

def smaller_than_3(x):
    return x < 3
    
group_obj = groupby(a, key=smaller_than_3)
# one line lambda
group_obj = groupby(a, key=lambda x: x<3)
for k,v in group_obj:
    print(k, list(val))

from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 15:
        break

a = [1,2,3]
for i in cycle(a):
    print(i)

for i in repeat(1, 4):
    print(i)
