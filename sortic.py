import sys
from termcolor import colored, cprint


def argum():
    a = []
    c = sys.argv[1]
    for i in c:
        if i != ' ':
            a.append(int(i))
    return a

def strr_(c):
    snew = ''
    l = ft_len(c)
    if c[-1] == ' ' and c[-2] == '!':
        for i in range(l - 2):
            snew += c[i]
    elif c[-1] == ' ':
        for i in range(l - 1):
            snew += c[i]
    return snew


def all_input_str():
    if ft_len(sys.argv) == 2:
        return strr_(sys.argv[1])[-1]
    ab = file_input()
    if ab != '':
        c = ''
        for i in ab:
            c += i
        return strr_(c)
    inputt = input()
    if ' ' in inputt:
        afg = ''
        for i in inputt:
            if i != ' ':
                afg += i + " "
        return strr_(afg)
    else:
        strtt = ''
        strtt += inputt + ' '
        while inputt != '!':
            inputt = input()
            strtt += inputt + " "
        return strr_(strtt)
        

def sp_input(c):
    a = []
    while c != '!':
        a.append(int(c))
        c = input()
    return a


def rem(strr):
    ch = strr[-1] + strr[-2]
    if ch == '\n':
        otvet = ''
        for i in range(ft_len(strr - 2)):
            otvet += i
        return otvet
    return strr


def ft_remove_str(str1, str2):
    b = 0
    a = ''
    for i in str1:
        if i in str2:
            b += 1
        else:
            a += i
    if ft_len(str1) == b:
        return False
    else:
        return a


def file_input():
    strrr = ''
    with open('input.txt', 'r') as f:
        for line in f:
            strrr += ft_remove_str(line + ' ', '\n')
    return strrr


def bsp_input(c):
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


def sorted1(a):
    n = 1
    spisok = a
    while n < ft_len(spisok):
        for i in range(ft_len(spisok) - n):
            if spisok[i] > spisok[i + 1]:
                spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
        n += 1
    return spisok


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
    print(f'a = {a}')
    print(f'b = {b}')
    while b != ft_rev_list(a_sort) and ft_len(a) > 2:
        lenn = ft_len(a)
        minn, maxx = ft_min_max(a)
        if a[0] == minn and lenn != 2:
            b = [a[0]] + b
            otv.append('pb')
            a1 = []
            for i in range(1, lenn):
                a1.append(a[i])
            a = a1
        elif a[-1] == minn and lenn != 2:
            a = ft_rshift_list(a)
            otv.append('rra')
        else:
            a = ft_lshift(a)
            otv.append('ra')
        print(f'a = {a}')
        print(f'b = {b}')
    lenn = ft_len(a)
    if lenn == 2 and a[0] > a[1]:
        otv.append('sa')
        a[0], a[1] = a[1], a[0]
        print(f'a = {a}')
        print(f'b = {b}')
    while a != ft_rev_list(a_sort):
        if b != []:
            a = [b[0]] + a
            otv.append('pa')
            b1 = []
            for i in range(1, ft_len(b)):
                b1.append(b[i])
            b = b1
        print(f'a = {a}')
        print(f'b = {b}')
    file_output(otv)
    return otv


def ft_rev_list(num):
    n = ft_len(num) // 2
    for i in range(0, n):
        a = -1 * (i + 1)
        t = num[i]
        num[i] = num[a]
        num[a] = t
    return num


def file_output(a):
    f = open('output.txt', 'w', encoding='utf8')
    f.writelines(a[0])
    for i in range(1, ft_len(a)):
        f.writelines('\n')
        f.writelines(a[i])
    f.close()


def _strr(c):
    fr = c
    if c[0] == ' ':
        fr = ''
        for i in range(1, ft_len(c)):
            fr += c[i]
    return fr

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


verf = all_input_str()
ver = sortic(str_to_lst(verf), sorted1(str_to_lst(verf)))
for i in ver:
    if i == 'pa':
        cprint(f'{i}', 'red')
    elif i == 'pb':
        cprint(f'{i}', 'green')
    elif i == 'sa':
        cprint(f'{i}', 'yellow')
    elif i == 'sb':
        cprint(f'{i}', 'blue')
    elif i == 'ss':
        cprint(f'{i}', 'magenta')
    elif i == 'ra':
        cprint(f'{i}', 'cyan')
    elif i == 'rb':
        cprint(f'{i}', 'grey')
    elif i == 'rr':
        cprint(f'{i}', 'white')
    elif i == 'rra':
        cprint(f'{i}', 'cyan')
    elif i == 'rrb':
        cprint(f'{i}', 'grey')
    elif i == 'rrr':
        cprint(f'{i}', 'white')
