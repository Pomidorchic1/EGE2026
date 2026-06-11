def f(x, steps):
    if x <= 16: return True
    if steps == 0: return False
    h = [f(x - 3, steps - 1),
         f(x - 8, steps - 1),
         f(x // 3, steps - 1)]
    return any(h) if (steps - 1) % 2 == 0 else all(h)

print('19)', [x for x in range(17, 200) if f(x, 2) and not f(x, 1)])
print('20)', [x for x in range(17, 200) if f(x, 3) and not f(x, 1)])
print('21)', [x for x in range(17, 200) if f(x, 4) and not f(x, 2)])