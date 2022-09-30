# 1.Задайте список из нескольких чисел.
# Напишите программу,которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

list = []
n = int(input("Введите размер списка: "))

for i in range(1, n + 1):
    list.append(random.randint(1, 10))
print(list)

sum_elem = 0

for i in range(0, len(list), 2):
    sum_elem += list[i]

print(sum_elem)
