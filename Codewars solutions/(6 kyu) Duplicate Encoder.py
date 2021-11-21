def duplicate_encode(word):
    duplicate = []
    for symb in word.lower():
        if word.lower().count(symb) == 1:
            duplicate.append('(')
        else:
            duplicate.append(')')
    return "".join(duplicate)
