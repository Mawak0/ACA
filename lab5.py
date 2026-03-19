import time
import matplotlib.pyplot as plt
from tqdm import tqdm

import random
import string

def naive_alg(string, substr):
    ind = []
    for i in range(0, len(string)):
        good = True
        for j in range(0, len(substr)):
            if string[i+j] != substr[j]:
                good = False
                break
        if good:
            ind.append(i)
    return ind


def boyer_moore(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return list(range(n + 1))
    last = {}
    for i, c in enumerate(pattern):
        last[c] = i
    matches = []
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            matches.append(i)
            if i + m < n:
                i += m - last.get(text[i + m], -1)
            else:
                i += 1
        else:
            i += max(1, j - last.get(text[i + j], -1))
    return matches


def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return list(range(n + 1))
    base = 256
    mod = 10**9 + 7
    h = pow(base, m - 1, mod)
    pat_hash = 0
    txt_hash = 0
    for i in range(m):
        pat_hash = (pat_hash * base + ord(pattern[i])) % mod
        txt_hash = (txt_hash * base + ord(text[i])) % mod
    matches = []
    for i in range(n - m + 1):
        if pat_hash == txt_hash and text[i:i + m] == pattern:
            matches.append(i)
        if i < n - m:
            txt_hash = (txt_hash - ord(text[i]) * h) % mod
            txt_hash = (txt_hash * base + ord(text[i + m])) % mod
            txt_hash = (txt_hash + mod) % mod
    return matches


def kmp(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return list(range(n + 1))
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    matches = []
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i - m + 1)
            j = pi[j - 1]
    return matches


def get_time_of_exec(func, arg):
    start_time = time.perf_counter()
    out = func(*arg)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return out, elapsed_time


def generate_string_with_substring(n, m, k):
    substring = ''.join(random.choices(string.ascii_lowercase, k=m))
    result = [''] * n
    positions = []
    available_positions = list(range(n - m + 1))

    for _ in range(k):
        pos = random.choice(available_positions)
        positions.append(pos)
        available_positions = [
            p for p in available_positions
            if p < pos - m + 1 or p > pos + m - 1
        ]

    for pos in positions:
        result[pos:pos + m] = list(substring)

    for i in range(n):
        if result[i] == '':
            result[i] = random.choice(string.ascii_lowercase)

    return ''.join(result), substring


run_range = range(100, 1000, 100)
naive_times = []
boyer_times = []
rabin_times = []
kmp_times = []

for n in run_range:
    st, substr = generate_string_with_substring(n, 10, 5)
    naive_times.append(get_time_of_exec(naive_alg, [st, substr])[1])
    boyer_times.append(get_time_of_exec(boyer_moore, [st, substr])[1])
    rabin_times.append(get_time_of_exec(rabin_karp, [st, substr])[1])
    kmp_times.append(get_time_of_exec(kmp, [st, substr])[1])

plt.plot(naive_times, label="Наивный алгоритм")
plt.plot(boyer_times, label="Алгоритм Бойера-Мура")
plt.plot(rabin_times, label="Алгоритм Рабина-Карпа")
plt.plot(kmp_times, label="Алгоритм Кнута-Морриса-Пратта")
plt.legend(loc='upper left', fontsize='medium')
plt.xlabel('Размер строки')
plt.ylabel('Время в сек.')
plt.show()
