def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'


ans = []

for N in range(1, 100_000):
    R = convert(N, 6)
    if sum(map(int,R)) % 5 == 0:
        R = R.replace('0', '*')
        R = R.replace('3', '0')
        R = R.replace('*', '3')
        R = '11' + R
    else:
        R = R[:1] + '05' + R[3:] + '44'
    R = int(R, 6)
    if R > 1500:
        ans.append([R, N])
print(max(ans, key=lambda x: (-x[0], x[1])))
