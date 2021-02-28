# This program will give you max length of continuous sequence

# Without using dictionary

def count_max(arr):
    count = 1
    arr.sort()
    temp_arr = []
    for i in range(len(arr)-1):
        # print(count, temp_arr)
        if arr[i] == arr[i+1] - 1:
            count += 1
        else:
            temp_arr.append(count)
            count = 1
    temp_arr.append(count)
    return max(temp_arr)


arr = [102, 4, 100, 1, 101, 3, 2, 103, 104, 105]
print(count_max(arr))

# with using dictionary


def count_max_with_dictionary(arr):
    dictionary = {}
    max_lenght = 0

    for i in arr:
        dictionary[i] = True

    for i in arr:
        dictionary[i] = False
        curr_len = 1
        left = i - 1
        right = i + 1

        while left in dictionary:
            dictionary[left] = False
            curr_len += 1
            left -= 1

        while right in dictionary:
            dictionary[right] = False
            curr_len += 1
            right += 1

        max_lenght = max(max_lenght, curr_len)
    print(max_lenght)


arr = [102, 4, 98, 99, 100, 1, 101, 3, 2, 103, 104, 105]

count_max_with_dictionary(arr)
