from math import log2, ceil

for N in range(1, 1000000):
    L = 172
    i = ceil(log2(N))
    I = ceil(i * L / 8)
    if 356_984 * I >= 54 * 2**20:
        print(N)
        break
