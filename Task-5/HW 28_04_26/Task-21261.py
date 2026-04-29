def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'


ans = []

for N in range(1, 100_000):
    R = convert(N, 4)
    if sum(map(int, R)) % 3 == 0:
        R = R.replace('0', '*')
        R = R.replace('2', '0')
        R = R.replace('*', '2')
        R = '32' + R
    else:
        R = R[:1] + '10' + R[3:] + '33'
    R = int(R, 4)
    if R > 320:
        ans.append([R, N])
print(max(ans, key=lambda x: (-x[0], x[1])))
