def inputt():
    a = []
    b = []
    i = input()
    while i != '!':
        a.append(int(i))
        i = input()
    i = input()
    while i != '*':
        b.append(int(i))
        i = input()
    return a, b


def sorted(lst):
    n = 1
    while n < ft_len(lst):
        for i in range(ft_len(lst) - n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


def ft_rshift_list(mass):
    n = ft_len(mass)
    p = mass[n - 1]
    for i in range(0, n):
        x = n - i - 1
        mass[x] = mass[x - 1]
    mass[0] = p
    return mass


def ft_len(lst):
    lenn = 0
    for i in lst:
        lenn += 1
    return lenn


def ft_lshift(a):
    a1 = a[0]
    lst = []
    for i in range(1, ft_len(a)):
        lst.append(a[i])
    lst.append(a1)
    return lst


def result(a, c):
    lst1 = a
    #a_sort = sorted(a)
    b = []
    #print(f'a = {a}')
    #print(f'b = {b}')
    try:
        for i in c:
            if i == 'sa':
                a[0], a[1] = a[1], a[0]
            elif i == 'pa':
                lenn = ft_len(b)
                a = [b[0]] + a
                a1 = []
                for i in range(1, lenn):
                    a1.append(b[i])
                b = a1
            elif i == 'ra':
                a = ft_lshift(a)
            elif i == 'pb':
                lenn = ft_len(a)
                b = [a[0]] + b
                a1 = []
                for i in range(1, lenn):
                    a1.append(a[i])
                #print(a1)
                a = a1
            elif i == 'rra':
                a = ft_rshift_list(a)
            #print(f'a = {a}')
            #print(f'b = {b}')
    except:
        return False
    if a == sorted(lst1):
        return True
    else:
        return False

print(result([2, 1, 3, 6, 5, 8], ['ra', 'pb', 'rra', 'pb', 'pb', 'ra', 'pb', 'sa', 'pa', 'pa', 'pa', 'pa']))    