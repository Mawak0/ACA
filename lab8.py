from itertools import combinations


def knapsack_bruteforce(items, W):
    # items: (id, weight, value)
    n = len(items)

    best_value = 0
    best_set = []

    for r in range(n + 1):
        for comb in combinations(items, r):
            total_w = sum(x[1] for x in comb)
            total_v = sum(x[2] for x in comb)  # O(2^n *2)

            if total_w <= W and total_v > best_value:
                best_value = total_v
                best_set = comb

    return best_set, best_value


items = [
    (1, 3, 25),
    (2, 2, 20),
    (3, 1, 15),
    (4, 4, 40),
]

print(knapsack_bruteforce(items, 5))


def knapsack_greedy(items, W):
    # items: (id, weight, value)

    def sort_f(x):
        return -(x[2] / x[1])  # value/weight

    items.sort(key=sort_f) # O(n*log(n))

    total_w = 0
    total_v = 0
    result = []

    for item in items:
        if total_w + item[1] <= W:
            result.append(item)
            total_w += item[1]
            total_v += item[2]

    return result, total_v


items = [
    (1, 3, 25),
    (2, 2, 20),
    (3, 1, 15),
    (4, 4, 40),
]

print(knapsack_greedy(items, 5))