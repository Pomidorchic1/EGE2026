ans = []
for N in range(1, 100_000):
    R = bin(N)[2:]
    if N % 2 == 0:  # чётное
        R = '10' + R
    else:  # нечётное
        R = '1' + R + '01'
    R = int(R, 2)
    if R <= 30:
        ans.append(N)
print(max(ans))
