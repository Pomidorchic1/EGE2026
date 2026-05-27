def f(x,y,steps):
    if x + y >= 65: return steps % 2 == 0
    if steps == 0: return False
    h = [f(x+1,y,steps-1),
         f(x,y+1,steps-1),
         f(x*3,y,steps-1),
         f(x,y*3,steps-1),]
    return any(h) if (steps-1) % 2 == 0 else all(h)

print('19)', [y for y in range (1,59) if f(6,y,2)]) #7
print('20)', [y for y in range (1,59) if f(6,y,3) and not f(6,y,1)][:2])
print('21)', min([y for y in range (1,59) if f(6,y,4) and not f(6,y,2)]))
