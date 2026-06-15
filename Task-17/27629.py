with open(r'files\17_27629.txt') as file:
    data = [int(i) for i in file]

max_43 = max([i for i in data if str(i)[-2:] == '43' and len(str(i)) == 4])

ans = []

for num1, num2 in zip(data, data[1:]):
    u1 = len(str(abs(num1))) == 4
    u2 = len(str(abs(num2))) == 4
    if u1 + u2 >= 1:
        if (num1 + num2) ** 2 < max_43 ** 2:
            ans.append((num1 + num2) ** 2)
print(len(ans), max(ans))
