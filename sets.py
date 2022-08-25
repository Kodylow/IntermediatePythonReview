# Sets: unordered, mutable, no duplicates
my_set = {0,1,2,3,4,5}

#trick to find out how many unique chars in a word
hello_set = set("Hello")

empty_set = set()
# mutable so can add and remove
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.remove(1) #use discard to not get key error
my_set.pop()

for i in my_set:
    if 1 not in my_set:
        print("no one")

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7,11}
# Union
u = odds.union(evens)

# Intersection
i = evens.intersection(primes)

# Difference of sets
diff = odds.difference(primes)
diff = odds.symmetric_difference(primes)

# Modify set in place
odds.update(primes)
evens.intersection_update(odds)
evens.difference_update(primes)
evens.symmetric_difference_update(odds)

# Subset
bool = setA.issubset(setB)
# Superset
bool = setA.issuperset(setB)
# Disjoint
bool = setA.isdisjoint(setB)

# Careful with copies, can be deep or shallow
setA = {1,2,3}
# shallow
setB = setA
# deep
setB = setA.copy()

# Immutable Set
a = frozenset([1,2,3,4])