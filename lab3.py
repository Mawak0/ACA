import time
import matplotlib.pyplot as plt
from tqdm import tqdm


def narayana_permutations(arr):
    permutations = [arr[::]]
    arr = arr[::]
    while True:
        max_i_arr = [i for i in range(0, len(arr) - 1) if arr[i] < arr[i + 1]]
        max_i_arr.append(-1)
        max_i = max(max_i_arr)
        if max_i == -1:
            return permutations
        find_min = float("inf")
        find_id = None
        for j in range(max_i, len(arr)):
            if arr[max_i] < arr[j]:
                if arr[j] < find_min:
                    find_min = arr[j]
                    find_id = j
        arr[find_id], arr[max_i] = arr[max_i], arr[find_id]
        arr[max_i + 1:] = arr[max_i + 1:][::-1]
        permutations.append(arr[::])


def trotter_permutations(arr):
    arr = arr[::]
    permutations = [arr[::]]
    directions = [0 for i in range(0, len(arr))]

    def get_mobil_elems():
        mobil = []
        for r in range(0, len(arr)):
            if directions[r] == 0 and r != 0 and arr[r - 1] < arr[r]:
                mobil.append(r)
            if directions[r] == 1 and r != len(arr) - 1 and arr[r + 1] < arr[r]:
                mobil.append(r)
        return mobil

    while True:
        mobil_elems = get_mobil_elems()
        if not mobil_elems:
            return permutations

        def a(e):
            return arr[e]

        max_mobil = max(mobil_elems, key=a)
        if directions[max_mobil] == 0:
            arr[max_mobil - 1], arr[max_mobil] = arr[max_mobil], arr[max_mobil - 1]
            directions[max_mobil - 1], directions[max_mobil] = directions[max_mobil], directions[max_mobil - 1]
            max_mobil -= 1
        if directions[max_mobil] == 1:
            arr[max_mobil + 1], arr[max_mobil] = arr[max_mobil], arr[max_mobil + 1]
            directions[max_mobil + 1], directions[max_mobil] = directions[max_mobil], directions[max_mobil + 1]
            max_mobil += 1
        permutations.append(arr[::])
        for i in range(0, len(arr)):
            if arr[i] > arr[max_mobil]:
                if directions[i] == 0:
                    directions[i] = 1
                elif directions[i] == 1:
                    directions[i] = 0


def inv_to_perm(inv):
    n = len(inv)
    elems = list(range(1, n + 1))
    perm = []
    for i, v in enumerate(inv):
        perm.append(elems.pop(v))
    return perm


def generate_permutations_by_inv(n):
    inv = [0] * n
    permutations = []
    while True:
        permutations.append(inv_to_perm(inv))
        i = n - 1
        while i >= 0:
            inv[i] += 1
            if inv[i] <= (n - 1 - i):
                break
            inv[i] = 0
            i -= 1
        if i < 0:
            break
    return permutations


def get_time_of_exec(func, arg):
    start_time = time.perf_counter()
    out = func(arg)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return out, elapsed_time


calc_range = range(1, 10, 1)

narayana_times = [get_time_of_exec(narayana_permutations, list(range(0, i)))[1] for i in tqdm(calc_range)]
trotter_times = [get_time_of_exec(trotter_permutations, list(range(0, i)))[1] for i in tqdm(calc_range)]
inv_times = [get_time_of_exec(generate_permutations_by_inv, i)[1] for i in tqdm(calc_range)]

plt.plot(narayana_times, label="Алгоритм Нарайана")
plt.plot(trotter_times, label="Алгоритм Джонсона-Троттера")
plt.plot(inv_times, label="Алгоритм вектора инверсий")
plt.legend(loc='upper left', fontsize='medium')
plt.xlabel('Размер входных данных')
plt.ylabel('Время в сек.')
plt.show()

# сгенерировать все возможные комбинации перестановок элементов
print(narayana_permutations([1,2,3]))

# задано n-элементов. Необходимо перебрать все возможные варианты выборки из этих элементов
def samples(array, n):
    per = trotter_permutations(array)
    return set([p[0:n] for p in per])

print(samples(["стол", "стул", "шкаф"], 2))
