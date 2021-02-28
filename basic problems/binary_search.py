def binary_search(arr, l, r, x):
    if l > r:
        print("not found")
    else:
        mid = (l+r)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid-1, x)
        elif arr[mid] < x:
            return binary_search(arr, mid+1, r, x)


arr = [10, 12, 1, 14, 25, 36, 4, 5]
arr.sort()
print(arr)
print(binary_search(arr, 0, len(arr)-1, 36))
