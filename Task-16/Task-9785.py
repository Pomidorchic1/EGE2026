from sys import setrecursionlimit
def f(n):
    if n < 7: return 7
    if n >=7: return n + 1 + f(n-2)
setrecursionlimit(1020)

print(f(2024) - f(2020))

print(2024 + 1 + 2022 + 1)