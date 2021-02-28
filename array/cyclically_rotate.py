def rotate_cyclically(array, n):
    for i in range(n):
        temp = array[-1]
        array = array[:-1]
        array.insert(0, temp)
    return array


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(rotate_cyclically(arr, 4))
