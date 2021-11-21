def is_triangle(a, b, c):
    n = [a, b, c]
    n.sort()
    if n[0] + n[1] > n[2]:
        return True
    else:
        return False
