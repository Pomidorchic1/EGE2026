def f(x, steps):
    if x >= 128: return steps % 2 == 0
    if steps == 0: return False
    h = [f(x + 2, steps - 1),
        f(x + 5, steps - 1),
        f(x * 2, steps - 1)]
    return any(h) if (steps - 1) % 2 == 0 else all(h)


print('19)', min([x for x in range(2, 127) if f(x, 2)]))
print('20)', [x for x in range(2, 127) if f(x, 3) and not f(x, 1)][:2])
print('21)', min([x for x in range(2, 127) if f(x, 4) and not f(x, 2)]))