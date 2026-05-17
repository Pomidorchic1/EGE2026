def convert (num,sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

cnt = 0

for N in range(int('1000',16),int('FFFF',16)):
    R = convert(N,16)
    if str(R).count('9') == 1:
                cnt +=1
print(cnt)