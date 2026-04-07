from turtle import *

screensize(10_000,10_000)
tracer(False)
lt(90)
m = 10

for i in range (3):
    fd(7 * m) # 8
    rt(90)
    fd(12 * m) # 13
    rt(90)

up()

fd(4 * m)
rt(90)
fd(6* m)
lt(90)

down()

for i in range(4):
    fd(83* m) # 84
    rt(90)
    fd(77* m) # 78
    rt(90)
down()
up()
for x in range (0,7):
    for y in range (0,4):
        goto (x * m, y * m)
        dot(3,"red")
print (8*13 + 78* 84 - (7 * 4))
update()

done()
