"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843."""

num = input("Введите натуральное число: ")
num_revers = ""
for i in range(len(num)-1, -1, -1):
    num_revers += num[i]
print(f"Число, обратное для числа {num}: {int(num_revers)}")
