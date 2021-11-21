def max_sequence(arr):
    max_sum = 0
    for i in range(len(arr)):
        summa = arr[i]
        max_sum = max(max_sum, summa)
        for k in range(i + 1, len(arr)):
            summa += arr[k]
            max_sum = max(max_sum, summa)
    return max_sum
