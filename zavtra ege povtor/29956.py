def f (num,sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res [::-1] if res else '0'

for N in range(1,100_000):
    R = f(N,3)
    if N % 3 == 0:
        R = '1' + '02'
    else:
        R = R + f(N % 3 * 5,3)
    R = int(R,3)
    if R >= 177:
        print(N)