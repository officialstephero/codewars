def printer_error(s):
    counter = 0
    for color in s:
        if 97 <= ord(color) <= 109:
            pass
        else:
            counter += 1
    return f'{counter}/{len(s)}'
