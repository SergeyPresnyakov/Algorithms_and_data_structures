"""1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными
числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут."""

import random, cProfile
array_2 = [random.randint(-100, 99) for i in range(1000)]


def sort_bubble(array):
    for j in (range(1, len(array))):
        for i in range(len(array) - j):
            if array[i] < array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]

    return(array)

print("sort_bubble")
array = array_2[:]
print(array)
print(sort_bubble(array))


print()
# Оптимизированный алгоритм
print("smart_sort_bubble")

def smart_sort_bubble(array):
    for j in (range(1, len(array))):
        is_sorted = True
        for i in range(len(array) - j):
            if array[i] < array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
                is_sorted = False

        if is_sorted:
            break
    return (array)

array = array_2[:]
print(array)
print(smart_sort_bubble(array))

print()
print("sort_bubble")
array = array_2[:]
cProfile.run('sort_bubble(array)')

print("smart_sort_bubble")
array = array_2[:]
cProfile.run('smart_sort_bubble(array)')

# sort_bubble
#          1004 function calls in 0.296 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.296    0.296 <string>:1(<module>)
#         1    0.295    0.295    0.296    0.296 lesson_7_task_1.py:12(sort_bubble)
#         1    0.000    0.000    0.296    0.296 {built-in method builtins.exec}
#      1000    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# smart_sort_bubble
#          991 function calls in 0.277 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.277    0.277 <string>:1(<module>)
#         1    0.277    0.277    0.277    0.277 lesson_7_task_1.py:30(smart_sort_bubble)
#         1    0.000    0.000    0.277    0.277 {built-in method builtins.exec}
#       987    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: мы видим, что умный алгоритм поволяет сократить количесвто циклов для сортировки с 1000 до 954.
# Однако это слабо увеличивает скорость сортировки (0.277 против 0.296)