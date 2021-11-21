def snail(snail_map):
    answer = []
    k = len(snail_map)
    if k % 2 == 0:
        while snail_map:
            answer.append(snail_map.pop(0))
            j = 0
            while j != len(snail_map) - 1:
                answer.append([snail_map[j].pop(-1)])
                j += 1
            answer.append(list(reversed(snail_map.pop(-1))))
            j = 1
            while j != len(snail_map) + 1:
                answer.append([snail_map[-j].pop(0)])
                j += 1

    else:
        while len(snail_map) != 1:
            answer.append(snail_map.pop(0))
            j = 0

            while j != len(snail_map) - 1:
                answer.append([snail_map[j].pop(-1)])
                j += 1
            answer.append(list(reversed(snail_map.pop(-1))))
            j = 1
            while j != len(snail_map) + 1:
                answer.append([snail_map[-j].pop(0)])
                j += 1
        answer.append(snail_map.pop())

    numbers = []
    for num in answer:
        for i in num:
            numbers.append(i)
    return numbers
