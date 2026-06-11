def f(cur,end):
    if cur < end or cur == 9 or cur == 16: return 0
    if cur == end: return 1
    if cur > end: return f(cur-1,end) + f(cur-2, end) + f(cur//3,end)

print(f(19,3))