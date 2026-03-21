# Работа с переменными

client_age = 55
clientAge = 10

# Типы данных

# Числа
# int / integer / целое число
my_int = 100
print(type(my_int))

# float / дробные числа / вещественные числа / с плавающей точкой
my_float = 5.5
print(type(my_float))

# complex / комплексные числа
my_complex = 2 + 2j
print(type(my_complex))

# Последовательности
# str / string / строка
my_str_1 = 'Hel"lo'
my_str_2 = "Hel'lo"
my_str_3 = '''Hello'''  # переносная строка
print(type(my_str_1))

# list / список
my_list = [1, 2.2, 3, 4, 'Test']
print(type(my_list))

#tuple / кортеж
my_tuple = (1, 2, 3, 4, '52')
print(type(my_tuple))

# Извлечение элемента последовательности.
# Обращаемся на нужную позицию по индексу.
# Индексация всегда начинается слева от 0.
print(my_str_1[0]) # Нулевой символ строки
print(my_list[3]) # Третий элемент списка
print(my_tuple[2]) # Второй элемент кортежа