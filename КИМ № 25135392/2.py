print('x y w z')

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F  = (w == z) or not(y <= w) or not x
                if not F:
                    print(x,y,w,z)