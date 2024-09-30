
def merge(a, begin, middle, end):
    l = [0] * (middle - begin)
    r = [0] * (end - middle)
    comps = 0
    moves = 0
    for i in range(begin, middle):
        moves += 1
        l[i - begin] = a[i]
    for i in range(middle, end):
        moves += 1
        r[i - middle] = a[i]
    k = begin
    li = 0
    ri = 0
    while li < middle - begin and ri < end - middle:
        comps += 1
        if l[li] < r[ri]:
            moves += 1
            a[k] = l[li]
            li += 1
        else:
            moves += 1
            a[k] = r[ri]
            ri += 1
        k += 1
    while li < middle - begin:
        moves += 1
        a[k] = l[li]
        li += 1
        k += 1
    while ri < end - middle:
        moves += 1
        a[k] = r[ri]
        ri += 1
        k += 1
    return a, comps, moves


def merge_sort_with_bounds(a, begin, end):
    if end - begin <= 1:
        return a, 0, 0
    middle = (end + begin) // 2
    a, cl, ml = merge_sort_with_bounds(a, begin, middle)
    a, cr, mr = merge_sort_with_bounds(a, middle, end)
    a, cm, mm = merge(a, begin, middle, end)
    return a, cl + cr + cm, ml + mr + mm


def merge_sort(a):
    return merge_sort_with_bounds(a, 0, len(a))




def merge_sort_optimized(a): pass 
def merge_sort_super_optimized(a): pass 
