for x in range(1, 27001):
    num = 3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3 - x
    k = 0
    while num > 0:
        if num % 27 == 0: k += 1
        num = num // 27
    if k == 6:
        print(x)
