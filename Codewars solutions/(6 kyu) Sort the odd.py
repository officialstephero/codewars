def sort_array(source_array):
    even = dict()
    odd = dict()
    k = 0
    for num in source_array:
        if num % 2 == 0:
            even[k] = num
        else:
            odd[k] = num
        k += 1
    odd_key = list(odd.keys())
    odd_values = list(odd.values())
    odd_values.sort()
    k = 0
    for key in odd_key:
        odd[key] = odd_values[k]
        k += 1
    res = {**even, **odd}
    answer = []
    for key in sorted(list(res.keys())):
        answer.append(res.get(key))

    return answer
