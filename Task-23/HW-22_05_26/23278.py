def f(x, steps):
    if x <= 16:
        return steps % 2 == 1
    if steps == 0:
        return False

    moves = [x - 3, x - 8, x // 3]
    results = [f(move, steps - 1) for move in moves]

    if steps == 1:  # ход Пети
        return any(results)
    else:  # ход Вани
        return all(results)


print('19)', min([x for x in range(17, 1000) if not f(x, 1) and f(x, 2)]))[ ]