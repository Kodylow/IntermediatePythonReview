# With a range of numbers from 1 to n inclusive, we can make n! permutations. By labelling them in order starting from 1, return the kth permutation.

# Brute Force
# O(n * n!) Time Complekity
import itertools
def kth_permutation_brute_force(n, k):
    permutations = list(itertools.permutations(range(1, n+1)))
    return ''.join(map(str, permutations[k-1]))

#Want to find the Kth permutation WITHOUT generating all the possible permutations
# O(n^2) Time Complexity
# O(n) Space Complexity
def kth_permutation(n, k):
    permutation = []
    unused = list(range(1, n+1))
    fact = [1] * (n+1)
    for i in range(1, n+1):
        fact[i] = i*fact[i-1]
    k -= 1
    while n > 0:
        part_length = fact[n]//n
        i = k//part_length
        permutation.append(unused[i])
        n -= 1
        k %= 
    return ''.join(map(str, permutation))