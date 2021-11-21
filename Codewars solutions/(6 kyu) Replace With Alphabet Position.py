def alphabet_position(text):
    text = text.lower()
    positions = []
    for symb in text:
        if 97 <= ord(symb) <= 122:
            positions.append(str(ord(symb) - 96))
    return " ".join(positions)
