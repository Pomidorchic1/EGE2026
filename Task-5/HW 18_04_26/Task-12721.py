def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'


ans = []

for N in range(1, 100_000):
    R = convert(N, 8)
    if (R.count('0') + R.count('2') + R.count('4') + R.count('6')) % 2 != 0:
        R = R[-3:] + '46'
    else:
        R = convert(N % 8 * 5, 8) + R
    R = int(R, 8)
    if N >= 80:
        ans.append(R)
print(min(ans))
