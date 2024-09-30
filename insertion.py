
import search 

def insertion_sort(t):
    comps = 0
    moves = 0
    if len(t) <= 1:
        return t, 0, 0
    for i in range(1, len(t)):
        j = i
        # swap until right position found...
        comps += 1
        while j >= 1 and t[j - 1] > t[j]:
            (t[j - 1], t[j]) = (t[j], t[j - 1])
            moves += 3
            j = j - 1
            comps += 1
    return t, comps, moves


def insertion_sort_optimized(t):
    if len(t) <= 1:
        return t, 0, 0
    comps = 0
    moves = 0
    for i in range(1, len(t)):
        j = i
        # find position
        p, c, m = search.dicho_find_pos(t, t[i], 0, i)
        comps += c
        moves += m
        # shift until position
        moves += 1
        v = t[i]
        for j in range(i, p, -1):
            moves += 1
            t[i] = t[i - 1]
        moves += 1
        t[p] = v
    return t, comps, moves




