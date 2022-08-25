# Dictionary: Key-Value pairs, Unordered, Mutable
mydict = {"name": "Max", "age": 28, "city": "New York"}

print(mydict["name"])

#add kv
mydict["email"] = "max@xyz.com"

# remove kv
del mydict["email"]
mydict.pop("city")

#check key in dict
if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["not_in_here"])
except:
    print("Error")

# loop through dict
for key in mydict:
    print(key)
for key in mydict.keys():
    print(key)
for val in mydict.values():
    print(val)
for k,v in mydict.items():
    print(k,v)

# copy a dict
# shallow copy, still points to old dict
my_dict_cpy = mydict

# deep copy
my_dict_cpy = dict(mydict)
my_dict_cpy = mydict.copy()

# update dictionaries
my_dict.update(my_dict_cpy)

# can also use tuples and numbers as keys, just can't use mutable structs like lists
new_dict = {("blah", 2): "thingy", 3:91274, "test": "testerino"}