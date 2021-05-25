import math


def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
    return True


n = int(input("Enter a number to check : "))
if is_prime(n):
    print("prime")
else:
    print("Not prime")
