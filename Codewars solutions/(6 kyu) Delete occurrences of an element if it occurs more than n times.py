def delete_nth(order,max_e):
    d = []
    for photo in order:
        if d.count(photo) <= max_e - 1:
            d.append(photo)
    return d
