n = int(input())
k = n - 1

for i in range(0, n):
    for j in range(0, k):
        print(end=" ")

    k = k - 1

    for j in range(0, i + 1):
        print("* ", end="")
    print()


def new_triangle(n):
    k = n-1
    for j in range(n):
        for i in range(k):
            print(end=" ")
        k = k-1
        for i in range(j+1):
            print("*", end="")
        for i in range(j):
            print("*", end="")
        print()


def smallest_method(n):
    print("using smallest method")
    for i in range(n):
        print(" "*(n-1-i), end="")
        print("*"*((i*2)+1))


new_triangle(n)
smallest_method(n)
