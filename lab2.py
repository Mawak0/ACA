

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

print(bubble_sort([3,2,1]))


