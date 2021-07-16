"""1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными
числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут."""

import random
array = [random.randint(-100, 99) for i in range(50)]

print()
print("sort_bubble")
def sort_bubble(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
        n += 1
    return(array)

print(array)
print(sort_bubble(array))

print()
# Оптимизированный алгоритм
print("smart_sort_bubble")
def smart_sort_bubble(array):
    for j in (range(1, len(array))):
        for i in range(len(array) - j):
            if array[i] < array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
    return(array)

print(array)
print(smart_sort_bubble(array))