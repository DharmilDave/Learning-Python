# without recursion
def fibo1(n):
    a = 0
    b = 1
    s = 0
    if n < 0:
        print("Invalid")
    elif n == 0:
        print(a)
    elif n == 1:
        print(b)
    else:
        for _ in range(0, n):
            print(s, end=",")
            a = b
            b = s
            s = a + b


n = int(input("Enter a number to print fibonacci series: "))
print("Without recursion")
fibo1(n)

# With recursion


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return (1)
    else:
        return (fibo(n-2)+fibo(n-1))


print("\nWith recursion")
for i in range(n):
    print(fibo(i), end=",")
