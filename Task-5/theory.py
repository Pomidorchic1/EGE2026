# Стандартные системы счисления ( 2, 8, 16, 10)

num = 50
# Двоичная система
print(bin(num)[2:]) # возвращает str
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
print(int(bin_num,2))
print(int(oct_num,8))
print(int(hex_num,16))
five_num = '4444'
print (int(five_num,5))