#4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите десятичное число: "))

number_toBinary = ""

while number > 0:
    number_toBinary = str(number % 2) + number_toBinary
    number = number // 2


print(f"В двоичной системе счисление  {number_toBinary}")