print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = not (x == (w and not z)) and (y == (x and not w))
                if F:
                    print(x,y,w,z)