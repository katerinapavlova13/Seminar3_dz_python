#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.[Негафибоначчи]
# Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Fn = F(n-2)+F(n-1).
# Fn = F(n+2)−F(n+1).


def Getfibonachi(number):
    list = [1, 0, 1]
    for i in range(1, number):
        list.append(list[len(list) - 1] + list[len(list) - 2])
        list.insert(0, list[1] - list[0])
    return list

list = Getfibonachi(8)
print(f'Список чисел Негафибоначчи и Фибоначчи: {list}')





# fib = 0
# fib1 = 1
# fib2 = 1

# number = int(input())

# print(fib, fib1, fib2, end=" ")

# for i in range(2, number):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=" ")