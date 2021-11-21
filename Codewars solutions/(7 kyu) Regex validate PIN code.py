def validate_pin(pin):
    counter = 0
    for num in pin:
        if 48 <= ord(num) <= 57:
            counter += 1
    if (counter == 4 or counter == 6) and counter == len(pin):
        return True
    else:
        return False
