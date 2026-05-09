from turtle import *

screensize(10_000,10_000)
lt(90)
tracer(False)
m = 20

fd(30 * m)
lt(60)
fd(24 * m)
rt(240)

fd(54 * m)
lt(120)
fd(24 * m)
lt(60)

up()

fd(30 * m)
rt(90)
fd(20 * m)
lt(90)

down()

for n in range(17):
    fd(6 * m)
    lt(90)
    fd(80 * m)
    lt(90)
up()

for x in range(-21, 5):
    for y in range(20, 40):
        goto(x * m, y * m, )
        dot(3, 'red')
update()
done()
