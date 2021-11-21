def rot90(matrix):
    return[list(reversed(col)) for col in zip(*matrix)]


def validate_battlefield(field):
    for m in range(4):
        for k in range(9):
            x, y = k, 0
            while x != 9 and y != 9:
                if field[x][y] == field[x + 1][y + 1] == 1:
                    return False
                else:
                    x += 1
                    y += 1
        field = rot90(field)

    control_list = {3: 2, 4: 1}
    d = {1: 0, 2: 0, 3: 0, 4: 0}
    for _ in range(2):
        for i in range(len(field)):
            maxim = 0
            if field[i].count(1) != 0:
                count = 1
                for j in range(len(field[i]) - 1):
                    if field[i][j] == field[i][j + 1] == 1:
                        count += 1
                    elif field[i][j] != field[i][j + 1] or j == len(field[i]) - 2:
                        if count <= 4:
                            d[count] += 1
                            count = 1
                        else:
                            return False
                if count <= 4:
                    d[count] += 1
                else:
                    return False
        field = rot90(field)
    counter = dict()
    for num in range(3, 5):
        counter[num] = d.get(num)

    summa = sum([i.count(1) for i in field])
    if summa == 20 and counter == control_list:
        return True
    else:
        return False
