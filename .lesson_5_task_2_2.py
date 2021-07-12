"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
представляется как массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""

# Умножение
from collections import Counter
import numpy as np

dict_16 = {'0': 0, '1': 1, '2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'A': 10,'B': 11,'C': 12,'D': 13,'E': 14,'F': 15}

dict_10 = {v:k for k, v in dict_16.items()}

num_1 = list(Counter(input("Введите первое число в шестнадцатеричной системе счисления: ")).elements())
num_2 = list(Counter(input("Введите второе число в шестнадцатеричной системе счисления: ")).elements())

num_1 = [dict_16[i] for i in num_1]
num_2 = [dict_16[i] for i in num_2]

if len(num_1) < len(num_2):
    num_1 = (len(num_2) - len(num_1)) * [0] + num_1
elif len(num_2) < len(num_1):
    num_2 = (len(num_1) - len(num_2)) * [0] + num_2

num_1_reverse = num_1
num_1_reverse.reverse()
num_1_10 = 0
for i in range(len(num_1_reverse)):
    num_1_10 += num_1_reverse[i] * 16**i

product = num_2
for i in range(num_1_10 -1 ):
    summa_10 = np.array(product) + np.array(num_2)
    summa_10 = [0] + list(summa_10)

    summa_16_1 = []
    summa_16_2 = len(summa_10) * [0]
    for element in range((len(summa_10) - 1), -1, -1):
        if summa_10[element] > 15:
            summa_16_1  = [summa_10[element] % 16] + summa_16_1
        else:
            summa_16_1  = [0] + summa_16_1

    summa_16_2 = len(summa_10) * [0]
    for element in range((len(summa_10) - 1), -1, -1):

        if summa_10[element] > 15:
            summa_16_2[element - 1] = summa_16_2[element - 1] + 1

    for element in range((len(summa_10) - 1), -1, -1):
        if summa_10[element] <= 15:
            summa_16_2[element] = summa_16_2[element] + summa_10[element] % 16

    summa_16 = np.array(summa_16_1) + np.array(summa_16_2)
    if summa_16[0] == 0:
        summa_16 = summa_16[1:]
    product = summa_16
    if len(num_2) < len(product):
        num_2 = [0] + num_2

if summa_16[0] == 0:
    summa_16 = summa_16[1:]
summa_16 = [dict_10[i] for i in summa_16]
summa_16 = ''.join(summa_16)
print(f"Произведение введенных чисел = {summa_16}")