def first_non_repeating_letter(string):
    for sym in string.lower():
        if string.lower().count(sym) == 1:
            return string[string.lower().index(sym)]
    return ''
