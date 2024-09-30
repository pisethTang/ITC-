import random 


def random_refill(a):
    for i in range(len(a)):
        a[i].random.randint(0, 5*len(a))
        
        
def random_list(n):
    return [random.randint(0, 3*n) for _ in range(0,n)]


def sorted_random_list(n):
    l = []
    v = random.randint(1,5)
    for _ in range(0,n):
        l.append(v)
        v += random.randint(1,5)
    return l 


def sorted_random_list_v2(n):
    l = [random.randint(0,5)]
    for i in range(1, n):
        l.append(l[i-1] + random.randint(0,5))
    return l 