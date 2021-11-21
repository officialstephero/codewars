def create_phone_number(n):
    n = [str(i) for i in n]
    n = "".join(n)
    return f'({n[:3]}) {n[3:6]}-{n[6:]}'
