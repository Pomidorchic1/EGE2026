def convert(num):
    res = ''
    while num:
        res = str(num % 8) + res
        num //= 8
    return res if res else '0'

ans = []
for N in range(1, 100000):
    octN = convert(N)
    if octN[0] == '5':
        new = ''.join('1' if c == '2' else '2' if c == '1' else c for c in octN)
        R = '11' + new
    else:
        R = '2' + octN[1:] + '10'
    R_val = int(R, 8)
    if R_val < 1354:
        ans.append(N)
print(max(ans))