from turtle import *

screensize(10_000, 10_000)
lt(90)
tracer(False)
m = 15
down()

for i in range(8):
    fd(16 * m)
    rt(90)
    fd(22 * m)
    rt(90)

up()

fd(5 * m)
rt(90)
fd(5 * m)
lt(90)

down()

for i in range(8):
    fd(52 * m)
    rt(90)
    fd(77 * m)
    rt(90)

up()

for x in range(5, 23):
    for y in range(5, 17):
        goto(x * m, y * m, )
        dot(3, 'red')
print((22 - 5) * (16 - 5))
update()
done()
