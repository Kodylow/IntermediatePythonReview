import timeit
#Tuple: ordered, immutable, allows duplicate elements
mytuple = tuple(["Max", 28, "Boston"])

for i in mytuple:
    if "Max" in mytuple:
        print("yes")
    print(len(mytuple))

print(mytuple.count('Max'))
apple_tuple = ('a', 'p', 'p', 'l', 'e', 's')
mytuple.index("l")

sliced_tuple = apple_tuple[2:4]

my_tuple = (0,1,2,3,4,5)
# destructure tuple, star takes everything not exlicitly destructured into a list
i1, *i2, i3 = my_tuple

# tuples are more efficient than lists
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))