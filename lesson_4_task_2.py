"""Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого
числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов."""

import timeit

# Нахождения i-го по счёту простого числа на основе решета Эратосфена
def sieve(n):
    sieve = set(range(2, n * 10))
    list_prime_num = []
    while len(list_prime_num) < n:
        prime = min(sieve)
        list_prime_num.append(prime)
        sieve -= set(range(prime, n * 10, prime))
    return list_prime_num[-1]

# "lesson_4_task_2.sieve(100)"
# 300 loops, best of 3: 2.05 msec per loop

# "lesson_4_task_2.sieve(200)"
# 300 loops, best of 3: 8.42 msec per loop

# lesson_4_task_2.sieve(300)
# 300 loops, best of 3: 11.8 msec per loop

# lesson_4_task_2.sieve(400)
# 300 loops, best of 3: 21 msec per loop


# Нахождения i-го по счёту простого числа на основе проверки простоты числа
def sieve_2(n):
    list_prime_num = []
    i = 2
    while len(list_prime_num) < n:
        k = 0
        for j in range(2, i // 2+1):
            if (i % j == 0):
                k = k+1
        if (k <= 0):
            list_prime_num.append(i)
        i += 1
    return list_prime_num[-1]



# "lesson_4_task_2.sieve_2(100)"
#300 loops, best of 3: 9.48 msec per loop

# "lesson_4_task_2.sieve_2(200)"
# 300 loops, best of 3: 51 msec per loop

# lesson_4_task_2.sieve_2(300)
# 300 loops, best of 3: 143 msec per loop

# lesson_4_task_2.sieve_2(400)
# 300 loops, best of 3: 284 msec per loop


"""Общий вывод:
Из двух алгоритмов быстрее оказался алгоритм на основе решета Эратосфена.
В среднем простое число под номером 400 он находил в 13,5 раз быстрее чем алгоритм, основанный
на проверке числа на прстоту. Также первый алгоритм оказался более простым. При увеличении номера 
искомого простого числа со 100 до 400, время его работы увеличилось всего в 10 раз.
У второго алгоритма сложность увеличилась в 30 раз"""

