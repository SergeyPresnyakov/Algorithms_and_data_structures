"""9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

import random
matrix = [[random.randint(0, 10) for item in range(6)] for row in range(5)]
matrix

for a in matrix:
    print(('{:>4d}' * 6).format(*a))

min_row = []
for j in range(len(matrix[0])):
    column = []
    for i, item in enumerate(matrix):
        column.append(matrix[i][j])
    min = column[0]
    for item in column:
        if min > item:
            min = item
    min_row.append(min)
print()
print(f"Список минимальных значений столбцов матрицы: {min_row}")
max = min_row[0]
for item in min_row:
    if max < item:
        max = item
print(f"Максимальный элемент среди минимальных элементов столбцов матрицы: {max}")