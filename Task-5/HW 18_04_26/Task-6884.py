ans = []
for N in range(1, 10000):
    r= bin(N)[2:]
    if N % 2 == 0:
        r = '1' + r + '0'
    else:
        r = '11' + r + '11'
    R = int(r, 2)
    if R > 225:
        ans.append(R)
print(min(ans))