from sys import setrecursionlimit


def f(n):
    if n == 1: return 1
    if n > 1: return (n + 1) * f(n - 1)


setrecursionlimit(6000)

print((f(2024) - 3 * f(2023)) / f(2022))

(2024 + 1) * f(2023)

f(2023) * ((2024 + 1) *  - 3)  / f(2022)

print ((2023 + 1) * ((2024 + 1) - 3)  )