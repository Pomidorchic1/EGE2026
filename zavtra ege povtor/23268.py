with open(r'23268.txt') as file:
    data = [list(map(int, i.split())) for i in file]
ans = []
for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 2, 2]:
        pov = [i for i in line if line.count == 2]
        if sum(pov) / 4 < max(line):
            ans.append(pos)
print(min(ans))
