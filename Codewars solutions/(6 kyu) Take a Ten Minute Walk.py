def is_valid_walk(walk):
    point = [0, 0]
    if len(walk) == 10:
        for direction in walk:
            if direction == 'n':
                point[1] += 1
            elif direction == 's':
                point[1] -= 1
            elif direction == 'w':
                point[0] += 1
            elif direction == 'e':
                point[0] -= 1
        if point == [0, 0]:
            return True
        else:
            return False
    else:
        return False
