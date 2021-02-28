def find_max(a):
    max = a[0]
    for item in a:
        if item > max:
            max = item
    return max


x = find_max([11, 15, 36, 21, 54, 85, 14, 10, 9, 65, 42])
print(x)
