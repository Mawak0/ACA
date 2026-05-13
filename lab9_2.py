def build_graph(cargos, incompatible_pairs):
    graph = {}

    for cargo in cargos:
        graph[cargo] = set()

    for pair in incompatible_pairs:
        graph[pair[0]].add(pair[1])
        graph[pair[1]].add(pair[0])

    return graph


def greedy_coloring(graph):
    def sort_f(v):
        return -len(graph[v])

    vertices = list(graph.keys())
    vertices.sort(key=sort_f)

    colors = {}

    for v in vertices:
        used_colors = set()

        for u in graph[v]:
            if u in colors:
                used_colors.add(colors[u])

        color = 1
        while color in used_colors:
            color += 1

        colors[v] = color

    return colors


def make_containers(colors):
    containers = {}

    for cargo in colors:
        container = colors[cargo]
        if container not in containers:
            containers[container] = []
        containers[container].append(cargo)

    return containers


def cargo_num(cargo):
    return int(cargo[1:])


cargos = ["g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10"]

incompatible_pairs = [
    ("g1", "g2"),
    ("g1", "g3"),
    ("g1", "g4"),
    ("g2", "g3"),
    ("g2", "g6"),
    ("g3", "g7"),
    ("g4", "g5"),
    ("g4", "g8"),
    ("g5", "g6"),
    ("g5", "g9"),
    ("g6", "g10"),
    ("g7", "g8"),
    ("g8", "g9"),
    ("g9", "g10"),
]

graph = build_graph(cargos, incompatible_pairs)
colors = greedy_coloring(graph)
containers = make_containers(colors)

print("Граф несовместимости:")
for cargo in cargos:
    print(cargo, sorted(graph[cargo], key=cargo_num))

print("Цвета:", colors)

print("Компоновка грузов по контейнерам:")
for container in sorted(containers):
    print(container, sorted(containers[container], key=cargo_num))

print("Количество контейнеров:", max(colors.values()))
print("Сложность: O(k + n * log(n) + n^2), где n - количество грузов, k - количество пар несовместимости")
