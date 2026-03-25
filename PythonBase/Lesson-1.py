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

# tuple / кортеж
my_tuple = (1, 2, 3, 4, '52')
print(type(my_tuple))

# Извлечение элемента последовательности.
# Обращаемся на нужную позицию по индексу.
# Индексация всегда начинается слева от 0.
print(my_str_1[0])  # Нулевой символ строки
print(my_list[3])  # Третий элемент списка
print(my_tuple[2])  # Второй элемент кортежа

test = ([8, 9, 'hello', 'lol'], ' good')
print(test[0][3][1])

# Множество
# set / Множество
# Хранит в себе только уникальные элементы
# Не упорядочены
my_set_1 = {1, 5, 2, 1, 1, 2, 3, 1, 1, 2, 3}
my_set_2 = {'k', 'l', 'l', 'e', "p"}
print(type(my_set_2))

# Словарь
# dict / dictionary / словарь
my_dict = {"name": "Anna", "age": 67}
print(type(my_dict))

# Логический
# boll/ boolean / Булевый/ Логический тип
my_bool_1 = True
my_bool_2 = False
print(type(my_bool_1))
