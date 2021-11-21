def decodeMorse(morse_code):
    results = []
    for item in morse_code.split(' '):
        if item != '':
            results.append(str(MORSE_CODE.get(item)))
        else:
            results.append(' ')
    answer = "".join(results).replace('  ', ' ', "".join(results).count('  '))

    while answer[0] == ' ' or answer[-1] == ' ':
        if answer[0] == ' ':
            answer = answer[1:]
        if answer[-1] == ' ':
            answer = answer[0:-1]

    return answer
