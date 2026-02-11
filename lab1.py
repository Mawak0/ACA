import matplotlib.pyplot as plt
import time

def iter_alg(n):
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return b

def fibonacci_recurs(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recurs(n - 1) + fibonacci_recurs(n - 2)


def get_time_of_exec(func, arg):
    start_time = time.perf_counter()
    out = func(arg)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return out, elapsed_time

calc_range = range(3, 40)
recurs_times = [get_time_of_exec(fibonacci_recurs, i)[1] for i in calc_range]
iter_times = [get_time_of_exec(iter_alg, i)[1] for i in calc_range]


plt.plot(recurs_times, label="Рекурсивный")
plt.plot(iter_times, label="Итеративный")
plt.legend(loc='upper left', fontsize='medium')
plt.xlabel('Порядковый номер числа последовательности')
plt. ylabel('Время в сек.')
plt.show()
