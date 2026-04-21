def convert (num,sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

ans = []

for N in range (11,100_000):
    R = convert(N,3)
    R_chet_2 = R.count('0') + R.count('2')
    R_ne_chet_2 = R.count('1')
    if  R_chet_2  > R_ne_chet_2:
        R = '22' + R
    else:
        R = '11' + R
    R = int(R,3)
    if  R > 100:
        ans.append(R)
print (min(ans))

# Зачем-то до этого считал сумму цифр :(
