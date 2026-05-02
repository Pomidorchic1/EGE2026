print('x y z w')
for x in range(2):
    for y in 0, 1:
        for z in (0,1):
            for w in [0,1]:
                F= not(w <= z) or (x<= y) or not x
                if F == 0:
                    print(x,y,z,w)