"""1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках
 домашнего задания первых трех уроков."""
# python -m timeit -n 1000 -s "import lesson_4_task_1" lesson_4_task_1.division_3(400)

import timeit, cProfile

def division(n):
    if n == 1:
        return 1
    else:
        return ((-1)**(n-1))/2**(n-1) + division(n - 1)

# "lesson_4_task_1.division(4)"
# 1000 loops, best of 3: 6.61 usec per loop

# "lesson_4_task_1.division(40)"
# 1000 loops, best of 3: 90.7 usec per loop

# "lesson_4_task_1.division(400)"
# 1000 loops, best of 3: 1.45 msec per loop



def division_2(n):
    i = 0
    range_number = 1
    sum = 0
    while i < n:
        sum += range_number
        range_number /= -2
        i += 1
    return sum

# "lesson_4_task_1.division_2(4)"
# 1000 loops, best of 3: 1.78 usec per loop

# "lesson_4_task_1.division_2(40)"
# 1000 loops, best of 3: 11.9 usec per loop


# "lesson_4_task_1.division_2(400)"
# 1000 loops, best of 3: 123 usec per loop



def division_3(n):
   sm=lambda k,n=1: n+sm(k-1,n/-2) if k>1 else n
   return sm(n)

# "lesson_4_task_1.division_3(4)"
#1000 loops, best of 3: 2.7 usec per loop

# "lesson_4_task_1.division_3(40)"
# 1000 loops, best of 3: 21.9 usec per loop

# "lesson_4_task_1.division_3(400)"
# 1000 loops, best of 3: 248 usec per loop



# division()

# cProfile.run('division(4)')
# 7 function calls (4 primitive calls) in 0.000 seconds
# 4/1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:6(division)

# cProfile.run('division(40)')
# 43 function calls (4 primitive calls) in 0.000 seconds
# 40/1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:6(division)

# cProfile.run('division(400)')
# 03 function calls (4 primitive calls) in 0.003 seconds
# 400/1    0.003    0.000    0.003    0.003 lesson_4_task_1.py:6(division)



# division_2()

# cProfile.run('division_2(4)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:23(division_2)

# cProfile.run('division_2(40)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:23(division_2)

# cProfile.run('division_2(4000)')
# function calls in 0.002 seconds
# 1    0.002    0.002    0.002    0.002 lesson_4_task_1.py:23(division_2)


# division_3()

# cProfile.run('division_3(4)')
# 8 function calls (5 primitive calls) in 0.000 seconds
# 4/1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:46(<lambda>)

# cProfile.run('division_3(40)')
# 44 function calls (5 primitive calls) in 0.000 seconds
# 40/1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:46(<lambda>)


# cProfile.run('division_3(400)')
# 404 function calls (5 primitive calls) in 0.001 seconds
# 400/1    0.001    0.000    0.001    0.001 lesson_4_task_1.py:46(<lambda>)


"""Общий вывод:
Из трех вариантов кода определения суммы n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… лучше всего
себя показал код с циклом while. Время его работы наименьшее при всех соответсвующих n и сложность O(n) - линейная.
Остальные алгоритмы работают дольше при одинаковых n поскольку и рекурсивная и лямбда функции вызывают себя
n раз. Рекурсивная функция также имеет линейную сложность O(n), а вот лямбда-функция имеет большую сложность.
Время ее работы меняется нелинейно при пропорцинальном изменении обхема входных данных"""