from turtle import *

screensize(10_000, 10_000)
lt(90)
tracer(False)
m = 15
down()

for i in range(2):
    fd(5 * m)  # 6
    lt(90)
    back(13 * m)  # 14
    lt(90)

up()

back(10 * m)
rt(90)
fd(9 * m)
lt(90)

down()

for i in range(2):
    fd(11 * m)  # 12
    rt(90)
    fd(7 * m)  # 8
    rt(90)

up()

for x in range(9, 14): #14 - 9 = 5
    for y in range(0, 2): # 2 - 0 = 2
        goto(x * m, y * m, )
        dot(3, 'red')
print((12 * 8 + 6 * 14) - 5 * 2)
update()
done()
