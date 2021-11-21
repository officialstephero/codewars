def find_uniq(arr):
    if arr.count(min(arr)) == 1:
        return min(arr)
    else:
        return max(arr)
