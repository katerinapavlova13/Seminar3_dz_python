#3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем
# *Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint, random

number = int(input('Введите количество элементов списка: '))
basis = []
def FindDifference():
    for i in range(number):
        result = round(random(), 2) + randint(0, number * 3)
        basis.append(result)
        if (i == 0):
            maximum = round(result - int(result), 2)
            minimum = round(result - int(result), 2)
        else:
            if ((result - int(result)) > maximum): maximum = round(result - int(result), 2)
            if ((result - int(result)) < minimum): minimum = round(result - int(result), 2)
    return (f"{basis}\n Pазница между максимальным значением {maximum} и минимальным значением {minimum}, равна => {round(abs(maximum-minimum), 2)}")


print(FindDifference())