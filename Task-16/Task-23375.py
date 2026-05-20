# F 42_999 = G (42_998) + G(42_996)
from sys import setrecursionlimit
setrecursionlimit(13000)
def g(n):
    if n <= 9: return 3 * n
    if n > 9: return g(n-4) + 2

def f(n):
    return g(n-1) + g(n-3)

print(f(42999))
