from turtle import *

screensize(5_000, 5_000)
tracer(False)
lt(90)
m = 10

for i in range(2):
    fd(13 * m) # 14
    rt(90)
    fd(20 * m) # 21
    rt(90)

up()
fd(8 * m)
rt(90)
bk(3 * m)
lt(90)
down()

for i in range(2):
    fd(16 * m) # 17
    rt(90)
    fd(8 * m) # 9
    rt(90)

up()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * m, y * m)
        dot(3, 'red')

print(14 * 21 + 17 * 9 - 6 * 6)
update()
done()