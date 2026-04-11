from turtle import *

screensize(100, 100)
left(90)
tracer(False)
m = 20
down()
for i in range(4):
    fd(10 * m)
    right(270)
up()
fd(3 * m)
right(270)
fd(5 * m)
right(90)
down()
for i in range(2):
    fd(10 * m)
    right(270)
    fd(12 * m)
    right(270)
up()

for x in range(-10, -4): # -4 - (- 10) = 6
    for y in range(3, 11): # 11 - 3 = 8
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()

print((11 * 11) + (11*13) - (6 * 8))
