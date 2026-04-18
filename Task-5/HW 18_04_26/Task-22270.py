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
        R = R.replace('1','*')
        R = R.replace('3','1')
        R= R.replace('*','3')
        R = '21' + R
    else:
        R = '1' + R[1:] + '12'
    R = int(R,4)
    if R < 598:
        ans.append([R,N])
print(max(ans))
