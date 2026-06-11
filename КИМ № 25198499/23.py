def f(cur, end):
    if cur == end: return 1
    if cur < end: return 0
    return f(cur - 3, end) + (f(cur // 2, end) if cur % 2 == 0 else 0)

print(f(27, 3) * f(63, 27))