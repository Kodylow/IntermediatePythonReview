from timeit import default_timer as timer
# Strings: ordered, immutable, text representation
my_string = 'hello world'

# multiline strings
multiline = """Hello \
World"""

char = my_string[0]
# immutable! the following doesn't work
# my_string[0] = 'h'

step_substring = my_string[::2]

for x in my_string:
    if x == 'e' && 'ell' in my_string:
        print("can find substrings in conditionals")

whitespace_str = 'hello           '

# strip whitespace
assert('hello' == whitespace_str.strip())

my_string.upper().lower()

my_string.startswith("h")
my_string.endswith("d")
my_string.find("o") # index 4
my_string.count("o") # 2
new = my_string.replace('world', 'universe') # returns a new string, doesn't mod in place

# String words to list and back, fast!!
my_list = my_string.split(" ")
start = timer()
new_string = " ".join(my_list)
stop = timer()
print(stop - start)

# Slow
start = timer()
new_string = ''
for i in my_list:
    new_string += i
stop = timer()
print(stop - start)

# Printing formatted strings
# %, .format(), f-Strings
var = 3.141592654
my_string = "the variable is %.2f" % var
my_string = "the variable is {:.2f}".format(var)

# fastest, newest way
my_string = f"the variable is {var}"
print(my_string)