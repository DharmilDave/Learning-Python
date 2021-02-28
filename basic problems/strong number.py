def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def is_strong_num(n):
    sum = 0
    temp = n
    while temp:
        rem = temp % 10
        sum += factorial(rem)
        temp = temp // 10

    if (sum == n):
        print("Strong number")
    else:
        print("Not")


n = int(input("Enter Number: "))
is_strong_num(n)
