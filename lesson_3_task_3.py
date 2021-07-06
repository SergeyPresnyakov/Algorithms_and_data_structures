"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random
array = [random.randint(0, 100) for i in range(10)]

print(f"Массив до изменения: {array}")
min = array[0]
max = array[0]
for item in array:
    if min > item:
        min = item
    elif max < item:
        max = item

min_index = array.index(min)
max_index = array.index(max)
array[min_index], array[max_index] = array[max_index], array[min_index]
print(f"Массив после изм-ия: {array}")

