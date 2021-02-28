
# *: 1st usage
def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# *: 2nd usage

numbers = (5, 6, 7, 8)

result = list(map(lambda x: x+x, numbers))
print(result)

# *: 3rd usage

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# * Lambda function usage


# fun = lambda x,y,z:x+y+z (Because it is being converted to simple function)


# print(fun(10, 12, 14))

# *: 4th usage

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)
