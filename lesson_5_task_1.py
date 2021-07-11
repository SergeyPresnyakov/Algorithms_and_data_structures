"""1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""

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