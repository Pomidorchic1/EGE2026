def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

ans = []

for N in range(1, 10000):
    R = convert(N, 4)
    if R[0] == '3':
        R = '1' = '3' and '3' = '1'
        R = '21' + R
    else:
