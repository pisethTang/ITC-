
def quick_choose_pivot(t, begin, end):
    return (begin+end)//2


def quick_sort_partition_in_place(t, begin, end):
    pivot_pos = quick_choose_pivot(t, begin, end)
    moves = 3
    t[begin], t[pivot_pos] = t[pivot_pos],t[begin]
    left = begin+1
    right = end-1
    comps = 0
    while right >= left:
        comps += 1
        if t[left] < t[begin]:
            left += 1
        else:
            comps += 1
            if t[right] >= t[begin]:
                right -= 1
            else:
                moves += 3
                t[left], t[right] = t[right], t[left]
                left += 1
                right -= 1
    moves += 1
    t[begin], t[right] = t[right], t[begin]
    return t, right, comps, moves

# this partition is not in place!
def quick_sort_partition(t, begin, end):
    pivot_pos = quick_choose_pivot(t, begin, end)
    l = []
    r = []
    comps = 0
    moves = 0
    for i in range(begin, pivot_pos):
        comps += 1
        moves += 1
        if t[i] < t[pivot_pos]:
            l.append(t[i])
        else:
            r.append(t[i])
    for i in range(pivot_pos+1, end):
        comps = 0
        moves = 0
        if t[i] < t[pivot_pos]:
            l.append(t[i])
        else:
            r.append(t[i])
    pivot = t[pivot_pos]
    moves += 1
    for i in range(0, len(l)):
        moves += 1
        t[begin+i] = l[i]
    moves += 1
    t[begin+len(l)] = pivot
    for i in range(0, len(r)):
        moves += 1
        t[begin+i+len(l)+1] = r[i]
    return t, begin+len(l), comps, moves


# strategy (recursive)
# - choose an element in the array (called the pivot)
# - arrange elements of the array such that
#   all element smaller than the pivot are on its left
#   and all element larger than the pivot are on its right
#   Note that at this point, pivot will be at its final location
# - recursive call to the two "sub-arrays"
def quick_sort_with_bounds(t, begin, end, partition):
    if end-begin <= 1:
        return t, 0, 0
    t, pivot_pos, c, m = partition(t, begin, end)
    t, cl, ml = quick_sort_with_bounds(t, begin, pivot_pos, partition)
    t, cr, mr = quick_sort_with_bounds(t, pivot_pos+1, end, partition)
    return t, c+cl+cr, m+ml+mr



def quick_sort(t, in_place=True):
    if in_place:
        return quick_sort_with_bounds(t, 0, len(t), quick_sort_partition_in_place)
    else:
        return quick_sort_with_bounds(t, 0, len(t), quick_sort_partition)


def quick_sort_optimised(a): pass 
