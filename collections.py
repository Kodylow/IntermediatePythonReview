# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

a = "aaaabbbbccc"
# creates dict with counts of each unique item
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)

#python3 normal dicts remember order, this is deprecated
from collections import OrderedDict


from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c']) # will return 0, default int type

from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)

d.pop()
d.popleft()
d.clear()
d.extend([4,5,6])
d.extendleft([1,2,3])

d.rotate(1) #moves everything 1 to the right
d.rotate(-1) # 1 left