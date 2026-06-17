with open(r'files\9.txt') as file:
    data = [list(map(int,i.split())) for i in file]
cnt = 0
for line in data:
    repeat = [line.count(i) for i in set(line)]
    if sorted(repeat) == [1,1,1,1,3]:
        nepov = [i for i in line if line.count(i) == 1]
        if max(line) in nepov:
            cnt += 1
print(cnt)