def next_bigger(n):
    for i in range(2, len(str(n)) + 1):
        g = number(i, n)
        if int(g[0]) > n:
            return answer(str(n)[:len(str(n)) - i], g[1], n)
    return -1


def number(i, n):
    c = "".join(sorted(str(n)[len(str(n)) - i:], reverse=True))
    c = str(c[0]) + str("".join(sorted(c[1:])))
    k = str(n)[:len(str(n)) - i] + str(c)
    return k, c


def answer(full_num, num, n):
    d = sorted(set(num), reverse=True)
    var = []
    while d:
        p = d.pop()
        num = list(num)
        a = num[0]
        b = num.index(p)
        c = num[num.index(p)]
        num[0], num[b] = c, a
        var.append("".join(num))
    var = [p[0] + "".join(sorted(list(p[1:]))) for p in var]
    for _ in var:
        if int(full_num + _) > n:
            return int(full_num + _)
    return -1
