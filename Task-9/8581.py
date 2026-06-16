with open(r'files\8581.txt') as file:
    data = [list(map(int, i.split())) for i in file]


for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 1, 3]:
        pov = [i for i in line if line.count != 1] # повторяющиеся числа
        non_pov = [i for i in line if line.count == 1] # не повторяющиеся числа
        if sum(non_pov) / 4 <=  pov[0]:
            print(sum(line))

