from turtle import *
screensize(10_000,10_000)
left (90)
m = 20
tracer(0)

for i in range(6):
    fd (33 * m)
    rt(90)
    fd(20* m)
    rt(90)
up()

fd(3*m)
rt(90)
fd(9*m)
lt(90)
down()
for i in range(6):
    fd(24*m)
    rt(90)
    fd(25*m)
    rt(90)

up()
for x in range(9,21):
    for y in range (3,28):
        goto(x *m, y*m)
        dot(4,'blue')
update()
done()