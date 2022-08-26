# Generators are function which return an iterator object. They generate the items inside the object lazily (one at a time and only when you ask for it, so much more memory efficient)

# generators are yielded not returned

def mygenerator():
    yield 1
    yield 2
    yield 3
    
g = mygenerator()

# generator runs to next yield statement, holds state and continues on next
value = next(g)
value2 = next(g)

# can pass a generator to anything that takes an iterable
print(sum(g))
sorted(g)


def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

# prints nothing
cd = countdown(4)
# prints 'Starting' then continues to yield
value = next(cd)


# compare generator to stored list
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

import sys

print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))


# Fibonacci sequence with generators

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

fib = fibonacci(30)
for i in fib:
    print(i)

# Generator comprehension
mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
    print(i)