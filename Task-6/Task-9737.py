from turtle import *
screensize(10_000, 10_000)
tracer(False)
lt(90)
m = 15
n = 2
for i in '/.':  # 0 1 / 5 6
    fd(10 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(5 * m)
rt(90)
fd(7 * m)
left(90)
down()
for i in range(2):
    fd(10 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()
for x in range(7, 15):
    for y in range(5, 11):
        goto(x * m, y * m)
        dot(3,'red')
print(11*19+ 11 * 8 - 6 * 8)

update()
done()
