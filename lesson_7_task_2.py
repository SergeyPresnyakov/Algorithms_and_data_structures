"""2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы."""

import random

# Создадим функцию для сортировки методом слияния
def sort_merge(arr):
    sorted_list_2 = []
    for i in range(len(arr)):
        sorted_list_2.append([arr[i]])

    while len(sorted_list_2) > 1:
        sorted_list = sorted_list_2
        sorted_list_2 = []
        for i in range(0, len(sorted_list) - 1, 2):
            sorted_list_3 = []
            a = sorted_list[i]
            b = sorted_list[i + 1]
            while True:
                if len(a) > 0 and len(b) > 0:
                    if a[0] >= b[0]:
                        sorted_list_3.append(b[0])
                        b.pop(0)
                        continue
                    elif a[0] < b[0]:
                        sorted_list_3.append(a[0])
                        a.pop(0)
                        continue
                elif len(a) == 0:
                    sorted_list_3 = sorted_list_3 + b
                    break
                elif len(b) == 0:
                    sorted_list_3 = sorted_list_3 + a
                    break

            sorted_list_2.append(sorted_list_3)

        if len(sorted_list) % 2 == 1:
            sorted_list_2.append(sorted_list[-1])

    sorted_list_2 = sorted_list_2[0]
    return sorted_list_2

# Сгенерируем одномерный вещественный массив, заданный случайными числами на промежутке [0; 50)
array = [round(random.random() * 50, 2) for i in range(50)]

# Отсортируем данный массив с помощью функции
sort_array = sort_merge(array)

print("Исходный массив:", array)
print("Отсортированный массив:", sort_array)
print()

# Проведем проверку
array.sort()
if array == sort_merge(array):
    print("Функция сортирует правильно")

# Исходный массив: [34.91, 18.47, 34.24, 10.15, 17.29, 13.06, 21.79, 16.04, 14.33, 19.15, 38.26, 49.23,
# 28.64, 23.27, 17.53, 8.66, 1.75, 2.76, 25.18, 33.59, 35.67, 10.79, 35.65, 34.16, 20.57, 41.2, 0.23, 27.44,
# 10.79, 12.67, 37.04, 16.29, 6.5, 48.72, 12.11, 27.82, 10.98, 29.62, 33.55, 40.68, 49.3, 16.35, 38.19, 37.02,
# 13.87, 27.29, 46.67, 2.96, 41.07, 46.03]

# Отсортированный массив: [0.23, 1.75, 2.76, 2.96, 6.5, 8.66, 10.15, 10.79, 10.79, 10.98, 12.11, 12.67,
# 13.06, 13.87, 14.33, 16.04, 16.29, 16.35, 17.29, 17.53, 18.47, 19.15, 20.57, 21.79, 23.27, 25.18, 27.29,
# 27.44, 27.82, 28.64, 29.62, 33.55, 33.59, 34.16, 34.24, 34.91, 35.65, 35.67, 37.02, 37.04, 38.19, 38.26,
# 40.68, 41.07, 41.2, 46.03, 46.67, 48.72, 49.23, 49.3]
#
# Функция сортирует правильно
#
# Process finished with exit code 0



