# lambda arguments: expression

add10 = lambda x: x + 10
print(add10(5))

# equivalent to
def add10_func(x):
    return x + 10

mult = lambda x,y: x*y
print(mult(2,7))

# sorted
points2D = [(1,2), (15,1), (5,-1)] 
points2D_x_sorted = sorted(points2D)
points2D_y_sorted = sorted(points2D, key=lambda x: x[1])

# sort by sum
points2D_sum_sorted = sorted(ponts2D, key=lambda x: x[0] + x[1])


# map(func, seq)
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

#equiv list comprehension
c = [x*2 for x in a]


# filter(func, seq)
# filter for evens
b = filter(lambda x: x%2==0, a)
# equiv list comprehension
c = [x for x in a if x%2==0]


# reduce(func, seq), repeatedly applies to elements and returns reduced value
from functools import reduce
product_a = reduce(lambda x,y: x*y, a)
print(product_a)