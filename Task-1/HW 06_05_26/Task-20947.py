from itertools import permutations
graph = 'АБ АВ БВ БГ ВД ЖГ ЖИ ЖД ГИ ИЕ ЕД '.split()
matrix = '267 157 468 356 248 134 12 35'.split()
print(*range(1,9))
for i in permutations('АБВГДЖИЕ'):
    if all(str(i.index(x) +1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 24 + 15
print(24+15)