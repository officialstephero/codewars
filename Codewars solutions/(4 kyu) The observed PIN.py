def get_pins(observed):
    from itertools import product

    neighbors = {0: [8], 1: [2, 4], 2: [1, 3, 5], 3: [2, 6],
                 4: [1, 5, 7], 5: [2, 4, 6, 8], 6: [3, 5, 9],
                 7: [4, 8], 8: [0, 5, 7, 9], 9: [6, 8]}
    numbers = []
    k = 0
    for num in observed:
        numbers.append([str(num)])
        for i in list(neighbors[int(num)]):
            numbers[k].append(str(i))
        k += 1

    asis = numbers[0]
    if len(numbers) > 1:
        for k in range(1, len(numbers)):
            asis = ["".join(p) for p in list(product(asis, numbers[k]))]

    return asis
