#2. Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

my_list = []
n = int(input("Введите размер списка: "))
def mix_list (my_list):
    for i in range(1, n + 1):
        my_list.append(random.randint(1, 10))
    return my_list
print(mix_list(my_list))
