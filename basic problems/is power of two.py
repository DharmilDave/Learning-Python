import math


def log2(x):
    if x == 0:
        return False
    else:
        return math.log10(x)/math.log10(2)


def is_power_of_two(n):
    if (math.ceil(log2(n)) == math.floor(log2(n))):
        print("Yes")
    else:
        print("No")


def is_power_of_two_(n):
    if n == 0:
        print("No")
        return
    while(n != 1):
        if (n % 2 != 0):
            print("No")
            return False
        n = n//2
    print("Yes")


is_power_of_two(49)
is_power_of_two_(0)
