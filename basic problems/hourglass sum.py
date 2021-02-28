def hourglassSum(arr):
    total = 0
    max_t = -100000
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (j+2) < 6 and (i+2) < 6:
                total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]+ arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                if total > max_t:
                    max_t = total

    return max_t

