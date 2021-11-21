def control_player(s):
    n = [0 for o in [i for k in s for i in k] for i in s[0] if len(set(i) & set(o)) > 1 and set(i) != set(o)]
    return True if len(n) == 0 else False


def count_player_in_day(d):
    s = [''.join(sorted(''.join(k))) for k in d]
    return False if [0 for i in range(len(s) - 1) if s[i] != s[i+1]] else True


def count_group_for_day(b):
    counter = [len(i) for i in b]
    return True if counter.count(max(counter)) == len(counter) else False


def valid(a):
    return bool(control_player(a)*count_player_in_day(a)*count_group_for_day(a))
