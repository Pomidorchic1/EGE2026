from turtle import *

left(90)
m = 10
tracer(0)
for i in range(2):
    fd(20 * m)
    left(270)
    fd(12 * m)
    rt(90)

up()

fd(9 * m)
rt(90)
fd(7 * m)
rt(90)

down()

for i in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()

for x in range(1,10):
    for y in range(0,10):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()
