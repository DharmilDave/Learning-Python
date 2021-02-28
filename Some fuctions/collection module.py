from collections import namedtuple
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import deque


a = "aaavbjkddbbbf"  # any iterables
b = "111232121321"
c_a = Counter(a)
c_b = Counter(b)
print(c_a, "\n", c_b)
# for k, v in c_a.items():
#     print(k, v)

# will give n most common items
print("1 Most common elements ", c_a.most_common(1))
# to get the particular element
print("Most common element :", c_a.most_common(2)[0][0])

print("2 Most common elements in b ", c_b.most_common(2))

# * namedtuple

Point = namedtuple('Point', 'x, y, z')
pt = Point(1, 4, 7)
print(pt)
# pt.y = 11  will not work as it is immutable
print(pt.y)

# * OrderedDict , in python 3.7 and above dict is same as OD
od = OrderedDict()
od["b"] = 2
od["c"] = 3
od["a"] = 4
print(od)


""" defaultdict: using this we can specify any defualt type for value, 
so if key is not yet in dict it will give default value instead of error """

dd_int = defaultdict(int)
dd_float = defaultdict(float)
dd_int["a"] = 1
dd_int["b"] = 2
dd_int["c"] = "a"  # will not give error
print(dd_int)
print(dd_int["d"])  # will give default value "0"

dd_float["a"] = 1
dd_float["b"] = 50
dd_float["c"] = "a"
print(dd_float)
print(dd_float["d"])


# * deque: double ended queue, it is iterable

dq = deque()
dq.append(1)
dq.append(2)
dq.append(3)
print(dq)
dq.appendleft(4)
print(dq)
dq.pop()  # pop from right
print(dq)
dq.popleft()
print(dq)
dq.clear()  # delete whole list
print(dq)
dq.extend([5, 6, 7])
print(dq)
dq.extendleft([-1, 0])
print(dq)
# will move all elements to "one" place right, we can do 2,-1,3 etc also
dq.rotate(1)
print(dq)
