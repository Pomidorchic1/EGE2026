with open(r'files\8981.txt') as file:
    data = [list(map(int,i.split())) for i in file]

ans = []

for line in data:
    if len(set(line)) == len(line):
        if 2 * (max(line) + min(line)) == sum(line) - max(line) - min(line):
            ans.append(line)
print(len(ans))
