def decode_bits(bits):
    import re
    bits = bits.strip('0')
    time_unit = min(len(m) for m in re.findall(r'1+|0+', bits))
    return bits[::time_unit].replace('111', '-').replace('1','.').replace('0000000','   ').replace('000',' ').replace('0','')

def decode_morse(morse_code):
    results = []
    for item in morse_code.split(' '):
        if item != '':
            results.append(str(MORSE_CODE.get(item)))
        else:
            results.append(' ')
    return "".join(results).replace('  ', ' ', "".join(results).count('  ')).strip()
