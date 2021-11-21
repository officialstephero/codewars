def solve_runes(runes):
    for i in range(10):
        try:
            if str(i) in runes:
                continue
            left_runes = runes[:runes.find('=')].replace('?', str(i))
            right_runes = runes[runes.find('=') + 1:].replace('?', str(i))
            if (right_runes.strip('-')[0] == '0' and len(right_runes) > 1) \
                    or (left_runes.strip('-')[0] == '0' and right_runes.strip('-')[0] != '0'):
                continue
            if eval(left_runes) == eval(right_runes):
                return int(i)
        except: continue

    return -1
