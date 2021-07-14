"""Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в
рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным
использованием памяти."""

'''
Возмем для анализа программу, где пользователь вводит данные о количестве предприятий, их наименования и 
прибыль за четыре квартала для каждого предприятия. Программа должна определить среднюю прибыль 
(за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''

#ВАРИАНТ №2

from collections import namedtuple, Counter
import numpy as np
num_enterprises = int((input("Укажите, количество предприятий, которое вы хотите ввести: ")))

enterprises = []
summa = 0
new_enterprises = namedtuple("new_enterprises", "name, profit_1_quarter, profit_2_quarter, profit_3_quarter, profit_4_quarter")
for i in range(num_enterprises):
    enterprises.append(new_enterprises(input(f"Введите название предприятия под номером {i+1}: "),
                                        int(input(f"Введите прибыль предприятия за 1 квартал : ")),
                                        int(input(f"Введите прибыль предприятия за 2 квартал: ")),
                                        int(input(f"Введите прибыль предприятия за 3 квартал: ")),
                                        int(input(f"Введите прибыль предприятия за 4 квартал: "))))
    summa += sum(list(Counter(enterprises[i][1:]).elements()))
print()
average_revenue = summa / num_enterprises
print(f"Средняя прибыль (за год для всех предприятий) = {average_revenue}")
print()
max = [name for name in [list(Counter(enterprises[i][:1]).elements()) for i in range(num_enterprises) if sum(list(Counter(enterprises[i][1:]).elements())) > average_revenue]]
min = [name for name in [list(Counter(enterprises[i][:1]).elements()) for i in range(num_enterprises) if sum(list(Counter(enterprises[i][1:]).elements())) <= average_revenue]]

print(f"Наименования предприятий, чья прибыль выше среднего: {list(np.array(max).flatten())}")
print()
print(f"Наименования предприятий, чья прибыль ниже либо равна средней: {list(np.array(min).flatten())}")

x = locals()

print()
import sys
print(f"Версия и разрядность ОС и интерпретатора Python: {sys.version, sys.platform}")

print()
import sys
total_memory = 0
for i in list(x):
    if (i[0] != "_") & (i[0] != "x") & (i != "total_memory") & (i != "sys") & (i != "namedtuple") & (i != "Counter") & (i != "np") & (i != "defaultdict"):
        print(f"Объем памяти, выделенный под переменную '{i}' = {sys.getsizeof(i)} байт")
        total_memory += sys.getsizeof(i)

print()
print("Общий объем памяти, выделенный под переменные =", total_memory, "байт")

# Версия и разрядность ОС и интерпретатора Python: ('3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)]', 'win32')
#
# Объем памяти, выделенный под переменную 'num_enterprises' = 64 байт
# Объем памяти, выделенный под переменную 'enterprises' = 60 байт
# Объем памяти, выделенный под переменную 'summa' = 54 байт
# Объем памяти, выделенный под переменную 'new_enterprises' = 64 байт
# Объем памяти, выделенный под переменную 'i' = 50 байт
# Объем памяти, выделенный под переменную 'average_revenue' = 64 байт
# Объем памяти, выделенный под переменную 'max' = 52 байт
# Объем памяти, выделенный под переменную 'min' = 52 байт
#
# Общий объем памяти, выделенный под переменные = 460 байт


