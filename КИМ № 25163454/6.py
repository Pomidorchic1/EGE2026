from turtle import *

screensize(10_000, 10_000)
left(90)
tracer(0)
m = 25
for i in range(2):
    fd(3 * m)
    lt(90)
    bk(10 * m)
    lt(90)
up()

bk(10 * m)
rt(90)
fd(8 * m)
lt(90)

down()

for i in range(2):
    fd(16 * m)
    rt(90)
    fd(8 * m)
    rt(90)
up()

for x in range(0,17):
    for y in range(-10,10):
        goto(x * m, y * m)
        dot(4,'blue')


update()
done()
