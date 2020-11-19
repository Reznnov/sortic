def sp_input():
    a = []
    c = input()
    while c != '!':
        a.append(int(c))
        c = input()
    return a


def bsp_input():
    c = input()
    a = []
    for i in c:
        if i != ' ':
            a.append(int(i))
    return a


def ft_len(lst):
    lenn = 0
    for i in lst:
        lenn += 1
    return lenn

def sorted(a):
    n = 1
    while n < ft_len(a):
        for i in range(ft_len(a) - n):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        n += 1
    return a
