from string import printable

for x in printable[1:13]:
    num_1 = int(f'9{x}ab', 13)
    num_2 = int(f'{x}46c', 16)
    num_3 = int(f'b7{x}', 15)
    num = num_1 + num_2 - num_3
    if num % 14 == 0:
        print(num // 14)