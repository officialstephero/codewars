def score(dice):
    scores = {'10': 1000, '60': 600, '50': 500, '40': 400, '30': 300, '20': 200,
              '11': 100, '51': 50}
    count = dict()
    for num in dice:
        count[num] = [dice.count(num) // 3, dice.count(num) - (dice.count(num) // 3) * 3]

    score_dict = dict()
    for key in list(count.keys()):
        for i in range(2):
            score_dict[str(key) + str(i)] = count[key][i]

    points = 0
    for key in score_dict:
        if int(score_dict[key]) != 0 and key in list(scores.keys()):
            points += int(score_dict[key]) * int(scores[key])

    return points
