def duplicate_num(arr):
    return max(set(arr), key=arr.count)


arr = [1, 2, 3, 4, 5, 4, 3, 3]
print(duplicate_num(arr))
