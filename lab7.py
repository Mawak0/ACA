def select_orders(orders, m):
    # orders: (id, profit, deadline)

    def sort_f(o):
        return -o[1]

    orders.sort(key=sort_f)

    days = [None] * m
    answer = []

    for o in orders:
        deadline = min(o[2], m)

        for d in range(deadline - 1, -1, -1):
            if days[d] is None:
                days[d] = o
                answer.append(o)
                break

    return answer


orders = [
    (1, 100, 2),
    (2, 50, 1),
    (3, 10, 2),
    (4, 20, 1),
]

print(select_orders(orders, 2))


def make_groups(children):
    # children: (id, age)

    def sort_f(c):
        return c[1]

    children.sort(key=sort_f)

    groups = []
    current_group = []
    start_age = None

    for c in children:
        if not current_group:
            current_group.append(c)
            start_age = c[1]
        elif c[1] - start_age <= 2:
            current_group.append(c)
        else:
            groups.append(current_group)
            current_group = [c]
            start_age = c[1]

    if current_group:
        groups.append(current_group)

    return groups


children = [
    (1, 5),
    (2, 6),
    (3, 7),
    (4, 10),
    (5, 11),
    (6, 13),
]

print(make_groups(children))