import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 10: return n
    return 3 * n + F(n - 3)

print((F(6250) + 2 * F(6244)) // F(6238))