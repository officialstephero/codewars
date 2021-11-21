def permutations(string):
    answer = {string}
    if len(string) == 2:
        answer.add(string[1] + string[0])

    elif len(string) > 2:
        for i, j in enumerate(string):
            for k in permutations(string[:i] + string[i + 1:]):
                answer.add(j + k)

    return list(answer)
