def f(x, y, steps):
    if x + y >= 211: return steps % 2 == 0
    if steps == 0: return False
    h = [
        f(x + 1, y, steps - 1),
        f(x, y + 1, steps - 1),
        f(x, y * 2, steps - 1),
        f(x * 2, y, steps - 1)
    ]
    return any(h) if (steps - 1) % 2 == 0 else all(h)


print('19', [x for x in range(1, 193) if f(x, 17, 2)])
print('20', [x for x in range(1, 193) if f(x, 17, 3) and not f(x, 17, 1)])
print('21', [x for x in range(1, 193) if f(x, 17, 4) and not f(x, 17, 2)])
