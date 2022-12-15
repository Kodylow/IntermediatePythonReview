# Given an integer n, generate all the valid combinations of n pairs of parentheses
# A combination that contains 1 type of parentheses is valid if every opening parenthesis has its closing parenthesis, and it doesn't have a closing parenthesis without having an unused opening parenthesis before it

# Check combination validity with a stack
def is_valid(combination):
    stack = []
    for par in combination:
            if par == '(':
                stack.append(par)
            else:
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
    return len(stack) == 0

# Backtracking Solution
# O(n * 2^n) Time Complexity
# O(n * 2^n) Space Complexity, callstack size + combs array size
def generate(n):
    def inner_func(n, diff, comb, combs):
        if diff < 0 or diff > n:
            return
        elif n == 0:
            if diff == 0:
                combs.append(''.join(comb))
        else:
            comb.append('(')
            inner_func(n-1, diff+1, comb, combs)
            comb.pop()
            comb.append(')')
            inner_func(n-1, diff-1, comb, combs)
            comb.pop()
    combs = []
    # pass 2*n for number of parentheses
    inner_func(2*n, 0, [], combs)
    return combs