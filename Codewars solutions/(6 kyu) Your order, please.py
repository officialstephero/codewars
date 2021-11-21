def order(sentence):
    sentence = sentence.split(' ')
    d = dict()
    for word in sentence:
        for i in range(len(word)):
            if 49 <= ord(word[i]) <= 57:
                d[int(word[i])] = word

    return " ".join([sorted(d.items(), key=lambda x: x[0])[i][1] for i in range(len(d))])
