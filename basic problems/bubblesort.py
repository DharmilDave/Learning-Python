def bubble_sort(arr):
    c = 0
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                c += 1

        if swapped == False:
            break
    print(f"Total {c} swaps required to sort the array.")
    print("Sorted array: {arr}")


arr = [5, 3, 18, 14, 6, 2]
bubble_sort(arr)
