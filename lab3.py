

def narayana_permutations(arr):
    arr = arr[::]
    step = False
    for i in range(0, len(arr)):
        find_min = float("inf")
        find_id = None
        for j in range(i, len(arr)):
            if arr[i] < arr[j]:
                if arr[j] < find_min:
                    find_min = arr[j]
                    find_id = j
        step = True
        arr[find_id], arr[i] = arr[i], arr[find_id]
        arr[i:find_min] = arr[i:find_min:-1]
    if not step:
        return arr