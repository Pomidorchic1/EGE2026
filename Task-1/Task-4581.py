from itertools import permutations

graph = 'AD DE EG GC CF FA AB BF BE '.split()
matrix = '37 367 125 56 34 247 126'.split()
print(*range(1, 8))

for comb in permutations('ABCDEFG'):
    if all(str(comb.index(x) + 1) in matrix[comb.index(y)] for x,y in graph):
        print(*comb)


# 13 + 53 = 66
