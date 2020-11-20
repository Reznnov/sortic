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


def ft_min_max(lst):
    minn = lst[0]
    maxx = lst[0]
    for i in lst:
        if i < minn:
            minn = i
        if i > maxx:
            maxx = i
    return minn, maxx


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


def ft_rshift_list(mass):
    n = ft_len(mass)
    p = mass[n - 1]
    for i in range(0, n):
        x = n - i - 1
        mass[x] = mass[x - 1]
    mass[0] = p
    return mass


def ft_lshift(a):
    a1 = a[0]
    lst = []
    for i in range(1, ft_len(a)):
        lst.append(a[i])
    lst.append(a1)
    return lst


def sortic(a, a_sort):
    otv = []
    b = []
    while b != a_sort[::-1]:
        lenn = ft_len(a)
        minn, maxx = ft_min_max(a)
        if a[0] == minn:
            b = [a[0]] + b
            otv.append('pb')
            a1 = []
            for i in range(1, lenn):
                a1.append(a[i])
            a = a1
        elif a[-1] == minn:
            a = ft_rshift_list(a)
            otv.append('rra')
        else:
            a = ft_lshift(a)
            otv.append('ra')
    print(b)
    return otv


print(sortic([2, 4, 3, 1, 5, 6], sorted([2, 4, 3, 1, 5, 6])))