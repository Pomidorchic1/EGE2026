def convert (num,sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res [::-1]

con = convert(51*7**12-7**3-22,7)
con_sum = sum(map(int, con))
print(con_sum )


num = 51*7**12-7**3-22
res = 0
while num:
    res += num % 7
    num //= 7
print (res)