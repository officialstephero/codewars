def song_decoder(song):
    song = song.split('WUB')
    d = []
    for elem in song:
        if elem != '':
            d.append(elem)
    return " ".join(d)
