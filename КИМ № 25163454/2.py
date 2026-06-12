print ('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = (not z and y and x and not w) or  ( not z and y and not x and not w) or (z and y and x and not w)
                if F:
                    print(x,y,w,z)
