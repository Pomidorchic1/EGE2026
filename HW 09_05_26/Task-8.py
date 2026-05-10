def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

cnt = 0

for N in range(int('1000000',9),int('8888888',9)):
    R = convert(N,9)
    if R[0] not in '1 3 5 7' :
        if R[-1] in '1 2 4 5 7 8':
            if R.count('6') > 0:
                cnt +=1
print(cnt)