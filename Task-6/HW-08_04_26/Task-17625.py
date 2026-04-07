from turtle import *

screensize(10_000, 10_000)
tracer(False)
lt(90)
m = 10

for i in range(10):
    fd(22 * m)
    rt(90)
    fd(16 * m)
    rt(90)

up()

fd(1 * m)
rt(90)
fd(1 * m)
lt(90)

down()

for i in range(10):
    fd(72 * m)
    rt(90)
    fd(79 * m)
    rt(90)
down()
up()
for x in range(1, 17):
    for y in range(1, 23):
        goto(x * m, y * m)
        dot(3, "red")

update()

done()

print((16 + 22) * 2 - 4)
