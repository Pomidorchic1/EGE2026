print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = (x or ((not z) and w) or w) == (y and (not x) and w)
                if F:
                    print(x,y,w,z)
