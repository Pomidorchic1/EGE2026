print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = x and (z <= w) and not y
                if F:
                    print(x, y, w, z)
                    # x w z y
