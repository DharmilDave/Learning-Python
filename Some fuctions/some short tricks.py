lis1 = [1, 2, 3, 6, 6, 5, 4, 1, 2, 5, 4, 8, 2, 5, 3, 1, 4, 4, 4]

lis2 = list(set(lis1))

most = max(set(lis1), key=lis1.count)
print(lis1, "\n No duplicates here \n", lis2)
print("Number which is occuring maximum times: ", most)

# list comrehension

odd_sqrs = [i**2 for i in lis2 if i % 2 == 1]
print("Squares of odd numbers in list 2:", odd_sqrs)

# multiple arguments


def sum(*a):
    s = 0
    for i in a:
        s = s + i
    print("sum:", s)


sum(10, 20)
sum(20, 22, 30)
sum(20, 25, 36, 32, 42, 44)

# reverse a string

a = "Hello everyone"
b = a[::-1]  # reversed it
print(a, "\n", b)

# find if a string is palindrome or not

string = "madam"
isPalindrome = string.find(string[::-1]) == 0
print(isPalindrome)

# using decrementing for loops

for i in reversed(range(1, 10)):  # method 1
    print(i)
for i in range(10, 1, -1):  # method 2
    print(i)
