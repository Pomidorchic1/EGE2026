from turtle import *

screensize(10_000,10_000)
tracer(False)
lt(90)
m = 10

for i in range (9):
    fd(22 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()
fd(1 * m)
rt(90)
fd(5* m)
lt(90)
down()

for i in range(9):
    fd(53* m)
    rt(90)
    fd(75* m)
    rt(90)
down()
up()
for x in range (0,2): # 2 - 0 = 2 - 1 = 1
    for y in range (0,22): # 22 - 0 = 22 - 1 = 21
        goto (x * m, y * m)
        dot(3,"red")

update()

done()

print((21+1) * 2)