def f(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

ans = []
for x in range(1, 2031):
    num_2 = f(6 ** 2030 + 6 ** 100 - x,6)
    ans.append(num_2.count('0'))
print(min(ans))
