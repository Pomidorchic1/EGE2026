from turtle import *

screensize(5_000, 5_000)
tracer(False)
lt(90)
m = 10

for i in range(2):
    fd(20 * m)
    lt(270)
    fd(12 * m)
    rt(90)

up()
fd(9 * m)
rt(90)
fd(7 * m)
lt(90)
down()

for i in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * m, y * m)
        dot(3, 'red')

print(13 * 21 + 14 * 7)
update()
done()