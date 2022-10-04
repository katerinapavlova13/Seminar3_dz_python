# 1. Задайте список из нескольких чисел.
# Напишите программу,которая найдёт сумму элементов списка, стоящих на нечётной позиции.(не индексах)
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 2, 5 и 3, ответ: 10

import random

list = []
number = int(input("Введите размер списка: "))
def mix_list (list):
    for i in range(1, number + 1):
        list.append(random.randint(1, 10))
    return list

#на нечетных позизиях(четных индексах)
def sum_elem_list(list):
    sum_elem = 0
    for i in range(len(list)):
        if i % 2 == 0:
            sum_elem += list[i]
    return sum_elem

print(mix_list(list))
print(f"Сумма элементов на нечетных позициях: {sum_elem_list(list)}")

#2вариант
#на нечетных позициях(четных индексах)

# def sum_elem_list(list):
#     sum_elem = 0
#     for i in range(0, len(list), 2):
#         sum_elem += list[i]

# на четных позициях(нечетных индексах)

    # for i in range(1, len(list), 2):
    #     sum_elem += list[i]
    #
    # return sum_elem

