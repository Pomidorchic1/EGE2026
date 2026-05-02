from itertools import permutations

graph = 'АБ БЕ ЕЖ ЖД ДВ ВА ГА ГБ ГД ГВ ДЕ БД'.split()
matrix = '256 13467 2456 237 136 1235 24'.split()
print(*range(1, 8))

for comb in permutations('АБВГДЕЖ'):
    if all(str(comb.index(x) + 1) in matrix[comb.index(y)] for x,y in graph):
        print(*comb)
