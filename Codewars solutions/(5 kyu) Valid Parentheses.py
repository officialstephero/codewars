def valid_parentheses(string):
    parentheses = [p for p in string if ord(p) == 40 or ord(p) == 41]
    if parentheses:
        if parentheses[0] == "(" and parentheses.count('(') == parentheses.count(')') \
                and parentheses[-1] == ")":
            while len(parentheses) >= 2 and (parentheses.count('(') != 0 or parentheses.count(')') != 0):
                parentheses = parentheses[parentheses.index('('):]
                parentheses.pop(parentheses.index(')'))
                parentheses.pop(parentheses.index('('))
        else:
            return False
        if parentheses:
            return False
        else:
            return True
    else:
        return True
