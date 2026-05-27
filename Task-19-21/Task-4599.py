def f(x, y, steps):
    if x + y >= 259: return steps % 2 == 0
    if steps == 0: return False
    h = [f(x + 1, y, steps - 1),
         f(x, y + 1, steps - 1),
         f(x * 2, y, steps - 1),
         f(x, y * 2, steps - 1)]
    return any(h) if (steps - 1) % 2 == 0 else all(h)

print('19)',[y for y in range (1,242) if f(17,y,2)]) #61
print('20)',[y for y in range (1,242) if f(17,y,3) and not f(17,y,1)])
print('20)',[y for y in range (1,242) if f(17,y,4) and not f(17,y,2)])



