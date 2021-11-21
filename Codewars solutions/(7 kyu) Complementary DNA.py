def DNA_strand(dna):
    d = []
    for sym in dna:
        if sym == 'A':
            d.append('T')
        elif sym == 'T':
            d.append('A')
        elif sym == 'C':
            d.append('G')
        elif sym == 'G':
            d.append('C')
    return "".join(d)
