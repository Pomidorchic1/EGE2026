from itertools import permutations

graph = 'AD DB BF FC CG GA BE FE CE GE'.split()
matrix = '47 357 2567 16 236 345 123'.split()
print(*range(1, 8))

for comb in permutations('ABCDEFG'):
    if all(str(comb.index(x) + 1) in matrix[comb.index(y)] for x,y in graph):
        print(*comb)



