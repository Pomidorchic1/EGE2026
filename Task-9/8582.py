with open(r'files\8582.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0

for line in data:
    amount = [line.count(i) for i in set(line)]  # подсчет сколько раз число повторяется
    if sorted(amount) == [1, 1, 1, 1, 3]:  # 4 разных и 1 повторяющееся числ
        if line.count(max(line)) == 1: # максимальное число повторяется 1 раз
            cnt += 1
print(cnt )
