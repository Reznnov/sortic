import sys
from termcolor import colored, cprint


def argum():
    a = []
    c = sys.argv[1]
    for i in c:
        if i != ' ':
            a.append(int(i))
    return a

def all_input():
    if ft_len(sys.argv) == 2:
        a = []
        c = sys.argv[1]
        for i in c:
            if i != ' ':
                a.append(int(i))
        return a
    ab = file_input()
    if ab != []:
        otvet = []
        for i in ab:
            otvet.append(int(i))
        return otvet
    inputt = input()
    if ' ' in inputt:
        return bsp_input(inputt)
    else:
        return sp_input(inputt)


def sp_input(c):
    a = []
    while c != '!':
        a.append(int(c))
        c = input()
    return a


def file_input():
    f = open('input.txt')
    a = []
    for i in f:
        a.append(int(i))
    return a


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


def sorted(a):
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
    while b != a_sort[::-1] and ft_len(a) > 2:
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
        print(otv)
        print(f'a = {a}')
        print(f'b = {b}')
    lenn = ft_len(a)
    if lenn == 2 and a[0] > a[1]:
        otv.append('sa')
        a[0], a[1] = a[1], a[0]
        print(f'a = {a}')
        print(f'b = {b}')
    while a != a_sort:
        if b != []:
            a = [b[0]] + a
            otv.append('pa')
            b1 = []
            for i in range(1, ft_len(b)):
                b1.append(b[i])
            b = b1
        print(f'a = {a}')
        print(f'b = {b}')
    return otv

def file_output(a):
    f = open('output.txt', 'w', encoding='utf8')
    f.writelines(a[0])
    for i in range(1, ft_len(a)):
        f.writelines('\n')
        f.writelines(a[i])
    f.close()

verf = all_input()
ver = sortic(verf, sorted(verf))
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
