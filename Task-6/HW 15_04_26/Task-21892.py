from turtle import *

screensize(10_000, 10_000)
tracer(False)
m = 50

for i in range (7):
    rt(45)
    fd(11 * m)
    rt(45)
up()
for x in range (-8,9):
    for y in range (-15,2):
        goto ( x * m, y * m)
        dot (3,'red')
print (7*7+8*8)
update()
done()

# Закономерность 7 по 7 и 8 по 8
