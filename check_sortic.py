def ft_len(lst):
    lenn = 0
    for i in lst:
        lenn += 1
    return lenn


def _strr(c):
    fr = c
    if c[0] == ' ':
        fr = ''
        for i in range(1, ft_len(c)):
            fr += c[i]
    return fr


def strr_(c):
    snew = ''
    l = ft_len(c)
    if c[-1] == ' ' and c[-2] == '!':
        for i in range(l - 3):
            snew += c[i]
    elif c[-1] == ' ' and c[-2] == '*':
        for i in range(l - 3):
            snew += c[i]
    elif c[-1] == ' ':
        for i in range(l - 1):
            snew += c[i]
    return snew


def all_input_str():
    inputt = input()
    strtt = ''
    strtt += inputt + ' '
    while inputt != '!':
        inputt = input()
        strtt += inputt + " "
    inputt = input()
    strtt1 = ''
    strtt1 += inputt + ' '
    while inputt != '*':
        inputt = input()
        strtt1 += inputt + " "
    return strr_(strtt), strr_(strtt1)


def inputt():
    spisok = ''
    sort = ''
    i = input()
    while i != '!':
        spisok += i
        i = input()
    i = input()
    while i != '*':
        sort += i
        i = input()
    return spisok, sort

"""def str_to_lst(str1, str2):
    spisok11 = []
    spisok22 = []
    for i in str1:
        if i != ' ':
            spisok11.append(int(i))
    for i in str2:
        spisok22.append(i)
    return spisok11, spisok22"""


def sorted1(lst):
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


def str_to_lst(strr):
    cdf = ''
    spp = []
    sp2 = []
    sp1 = []
    l = ft_len(strr)
    for i in range(l):
        if strr[i] == ' ':
            spp.append(i)
    nac = 0
    for i in spp:
        cdf = ''
        for j in range(nac, i):
            cdf += strr[j]
        nac = i
        sp1.append(_strr(cdf))
    cdf = ''
    for i in range(spp[-1] + 1, ft_len(strr)):
        cdf += strr[i]
    sp1.append(cdf)
    for i in sp1:
        sp2.append(int(i))
    return sp2


def str_to_lst2(strr):
    cdf = ''
    spp = []
    sp2 = []
    sp1 = []
    l = ft_len(strr)
    for i in range(l):
        if strr[i] == ' ':
            spp.append(i)
    nac = 0
    for i in spp:
        cdf = ''
        for j in range(nac, i):
            cdf += strr[j]
        nac = i
        sp1.append(_strr(cdf))
    cdf = ''
    for i in range(spp[-1] + 1, ft_len(strr)):
        cdf += strr[i]
    sp1.append(cdf)
    for i in sp1:
        sp2.append(i)
    return sp2


def ft_lshift(a):
    a1 = a[0]
    lst = []
    for i in range(1, ft_len(a)):
        lst.append(a[i])
    lst.append(a1)
    return lst


def result(a, c):
    Boll = True
    lst1 = a
    b = []
    try:
        for i in c:
            if i == 'sa':
                a[0], a[1] = a[1], a[0]
            elif i == 'sb':
                b[0], b[1] = b[1], b[0]
            elif i == 'ss':
                a[0], a[1] = a[1], a[0]
                b[0], b[1] = b[1], b[0]
            elif i == 'rb':
                b = ft_lshift(b)
            elif i == 'rrb':
                b = ft_rshift_list(b)
            elif i == 'rr':
                a = ft_lshift(a)
                b = ft_lshift(b)
            elif i == 'rrr':
                a = ft_rshift_list(a)
                b = ft_rshift_list(b)
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
                a = a1
            elif i == 'rra':
                a = ft_rshift_list(a)
    except:
        return False
    if a == sorted1(lst1):
        return True
    else:
        return False

strr1, strr2 = all_input_str()
sp1 = str_to_lst(strr1)
sp2 = str_to_lst2(strr2)
print(result(sp1, sp2))