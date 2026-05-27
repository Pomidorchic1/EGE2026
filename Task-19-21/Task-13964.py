from math import ceil


def f(x, y, steps):
    if x + y <= 108: return steps % 2 == 0
    if steps == 0: return False
    h = [f(x - 2, y, steps - 1),
         f(x, y - 2, steps - 1),
         f(ceil(x / 2), y, steps - 1),
         f(x, ceil(y / 2), steps - 1), ]
    return any(h) if (steps - 1) % 2 == 0 else all(h)


print('19)', max([y for y in range(49, 10000) if f(60, y, 2)])) # 192
print('20)', [y for y in range(49, 10000) if f(60, y, 3) and not f(60,y,1)])
print('21)', max([y for y in range(49, 10000) if f(60, y, 4) and not f(60,y,2)]))

