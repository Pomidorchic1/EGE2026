for x in range(1, 10000)[::-1]:
    num = 6 ** 900 + 6 ** 10 - x
    cnt_3 = cnt_5 = 0
    while num:
        if num % 6 == 3: cnt_3+=1
        elif num % 6 == 5: cnt_5+=1
        num //= 6
    if cnt_3 == cnt_5:
        print(x)
        break
