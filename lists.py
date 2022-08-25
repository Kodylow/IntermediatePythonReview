# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(len(mylist))
mylist.append("lemmon")
print(len(mylist))
mylist.insert(3, "blueberry")
mylist.pop()
mylist.remove("cherry")


for x in mylist:
    print(x)

if "banana" in mylist:
    print("banana in list")
else:
    print("banana not in list")
mylist.reverse()
mylist.sort()
mylist.clear()

mylist = [0] * 5

mylist2 = [1,2,3,4,5]
new_list = mylist + mylist2

# Slicing
a = new_list[4:]

# Step index
stepped = mylist[::-2]

# Copy list
list_cpy = mylist[:]

# List comprehension
comp_list = [i**2 for i in list_cpy]