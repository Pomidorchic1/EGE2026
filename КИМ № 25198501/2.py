print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = (not z or (y and not x)) or w
                if not F:
                    print(x, y, w, z)
