def f(n, e):
    if n == e: return 1
    if n < e or n == 8: return 0
    if n > e: return f(n - 1, e) + f(n - 4, e) + f(n // 3, e)

print(f(19,14)* f(14,2))