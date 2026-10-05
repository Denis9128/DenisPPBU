def fact(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(3))


def name(nm):
    cnt = 0
    def surname(snm):
        nonlocal cnt
#        global cnt
        cnt += 1
        print(cnt, nm, snm)
    return surname

cnt = 1000
sur = name("mary")
sur1 = name("Dasha")
sur("Petrova")
sur("sidorova")
