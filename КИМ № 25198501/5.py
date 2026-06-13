def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

ans = []

for N in range(10, 100000):
    tri = convert(N, 3)
    if N % 4 == 0:
        tri = tri + tri[-3:]
    else:
        tri = '1' + tri + '20'
    R = int(tri, 3)
    if R > 423:
        ans.append(R)

print(min(ans))