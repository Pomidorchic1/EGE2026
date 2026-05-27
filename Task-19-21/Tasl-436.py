def f(x, y, steps):
    if x + y >= 44: return steps % 2 == 0
    if steps == 0: return False
    h = [f(x + y, y, steps - 1),
         f(x, y + x, steps - 1),
         ]
    return any(h) if (steps - 1) % 2 == 0 else all(h)

print('19)', min([y for y in range(1,44) if f(11,y,1)]))
print('20)', min([y for y in range(1,44) if f(11,y,2)]))
print('21)', [(x,y) for y in range(1,44) for x in range(1,44) if f(x,y,3) and x-y == 0])
