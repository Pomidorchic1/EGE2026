from itertools import permutations
graph = 'AF FE ED DC CB BG AG FG EG DG CG'.split()
matrix = '345 467 14 123567 147 24 245'.split()
print(*range(1,8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) +1) in matrix[i.index(y)] for x, y in graph):
        print(*i)