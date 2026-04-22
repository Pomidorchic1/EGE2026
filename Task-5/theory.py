# Стандартные системы счисления ( 2, 8, 16, 10)

num = 50
# Двоичная система
print(bin(num)[2:])  # возвращает str
print(f'{num:b}')
# Восьмеричная система исчесления
print(oct(num)[2:])
print(f'{num:o}')
# Шестнадцатеричная система
print(hex(num)[2:])
print(f'{num:x}')

# Десятичная система
bin_num = '11011100'
oct_num = '23756'
hex_num = 'a1f9'
print(int(bin_num, 2))
print(int(oct_num, 8))
print(int(hex_num, 16))
five_num = '4444'
print(int(five_num, 5))


# Перевод в любую систему из 10 (2 <= sys <= 9)
def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'


print(convert(50, 3))

# Перевод в любую систему из 10 (2 <= sys <= 36)
from string import printable


def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1] if res else '0'


print(convert(50, 3))

# Полезные алгоритмы

# Сумма цифр двоичной записи
R = ' 10101000101010'
summ = R.count('1')

# Сумма цифр в любой системе (до 10)
R = '1234567890'
summ = sum(map(int, R))

# Сумма цифр в любой системе (до 36)
R = 'ABC5'
summ = sum(map(lambda x: int(x, 36), R))

# Усложненные вопросы задания
R, N = 10, 20
ans = []
ans.append([R, N])
# Максимальный N при максимальном R
print(max(ans))
# Минимальный N при минимальном R
print(min(ans))
# Минимальный N при максимальном R
print(max(ans, key=lambda x: (x[0], -x[1]))
# Максимальный N при минимальном  R
print(min(ans, key=lambda x: (x[0], -x[1]))
