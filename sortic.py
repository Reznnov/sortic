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