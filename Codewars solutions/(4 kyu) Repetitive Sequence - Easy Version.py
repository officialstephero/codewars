def find(n):
    d = [0, 1, 2, 2]
    d_sum = 5
    d_len = 4
    for i in range(3, n+1):
        d_sum += i * d[i]
        if d_sum >= n != 3:
            return d_len + d[i] - (d_sum - n) // i - 1
        d_len += d[i]
        if d_len < 69763:
            d += [i]*d[i]
    return d[n]
