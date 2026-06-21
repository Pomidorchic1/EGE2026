def f(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'


ans = []
for N in range(1, 100_000):
    R = f(N, 2)
    if N % 3 == 0:
        R = R + R[3:]
    else:
        R = R + f(N % 3 * 3, 2)
    R = int(R, 2)
    if 120 < R < 140:
        print(R,N)
