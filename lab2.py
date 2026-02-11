import matplotlib.pyplot as plt
import time
import random

def bubble_sort(array):
    iter_counter = 0
    while True:
        edit = False
        for i in range(0, len(array)-1-iter_counter):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                edit = True
        if not edit:
            return array
        iter_counter += 1



def gnome_sort(array):
    i = 0
    while True:
        if array[i] <= array[i+1]:
            i += 1
            if i == len(array)-1:
                return array
        else:
            array[i+1], array[i] = array[i], array[i+1]
            if i == 0:
                i += 1
            else:
                i -= 1

def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
    return nums


def get_time_of_exec(func, arg):
    start_time = time.perf_counter()
    out = func(arg)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return out, elapsed_time


def nearly_sorted(n, swaps_ratio=0.01):
    arr = list(range(n))
    swaps = int(n * swaps_ratio)
    for _ in range(swaps):
        i = random.randrange(n)
        j = random.randrange(n)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


res_bubble = []
res_gnome = []
res_insertion = []
res_bubble_nearly = []
res_gnome_nearly = []
res_insertion_nearly = []
ran = range(100, 1000, 100)
for n in ran:
    array = list(range(1, n))
    random.shuffle(array)
    nearly_sorted_array = nearly_sorted(n)

    res_bubble.append(get_time_of_exec(bubble_sort, array[::])[1])
    res_gnome.append(get_time_of_exec(gnome_sort, array[::])[1])
    res_insertion.append(get_time_of_exec(insertion_sort, array[::])[1])

    res_bubble_nearly.append(get_time_of_exec(bubble_sort, nearly_sorted_array[::])[1])
    res_gnome_nearly.append(get_time_of_exec(gnome_sort, nearly_sorted_array[::])[1])
    res_insertion_nearly.append(get_time_of_exec(insertion_sort, nearly_sorted_array[::])[1])


plt.plot(ran, res_bubble, label="Bubble sort", color="red")
plt.plot(ran, res_gnome, label="Gnome sort", color="green")
plt.plot(ran, res_insertion, label="Insertion sort", color="blue")

plt.plot(ran, res_bubble_nearly, label="Bubble sort nearly sorted", ls="dashed", color="red")
plt.plot(ran, res_gnome_nearly, label="Gnome sort nearly sorted", ls="dashed", color="green")
plt.plot(ran, res_insertion_nearly, label="Insertion sort nearly sorted", ls="dashed", color="blue")

plt.legend(loc='upper left', fontsize='medium')
plt.xlabel("Количество элементов массива")
plt. ylabel('Время в сек.')
plt.show()
