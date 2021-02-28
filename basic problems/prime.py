import math


def is_prime(n):
    is_p = False
    if n <= 0:
        print("not valid")
    elif n == 1:
        print("not defined")
    elif n == 2:
        print("prime")
    else:
        sqr = int(math.sqrt(n))
        for i in range(2, sqr):
            if n % i == 0:
                is_p = True
                break
        if is_p:
            print("prime")
        else:
            print("not prime")


n = int(input("Enter a number to check : "))
is_prime(n)
