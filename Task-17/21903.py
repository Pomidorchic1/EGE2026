with open(r'files\17_21903.txt') as file:
    data = [int(i) for i in file]

min_15 = min([i for i in data if str(abs(i))[-2:] == '15' and len(str(abs(i))) == 3])

ans = []

for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = num1 < 0
    u2 = num2 < 0
    u3 = num3 < 0
    if u1 + u2 + u3 == 0 or u1 + u2 + u3 == 3:
        if min(num1, num2, num3) * max(num1, num2, num3) > min_15 ** 2:
            ans.append(min(num1, num2, num3) * max(num1, num2, num3))
print(len(ans), min(ans))