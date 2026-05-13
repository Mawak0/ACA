def build_graph(mechanisms, jobs):
    graph = {}

    for job in jobs:
        graph[job] = set()

    for mechanism in mechanisms:
        works = mechanisms[mechanism]
        for i in range(0, len(works)):
            for j in range(i + 1, len(works)):
                graph[works[i]].add(works[j])
                graph[works[j]].add(works[i])

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


def make_schedule(colors):
    schedule = {}

    for job in colors:
        color = colors[job]
        if color not in schedule:
            schedule[color] = []
        schedule[color].append(job)

    return schedule


def job_num(job):
    return int(job[1:])


jobs = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10"]

mechanisms = {
    "b1": ["a1", "a4", "a6", "a10"],
    "b2": ["a2", "a3", "a7", "a9"],
    "b3": ["a2", "a5", "a8"],
    "b4": ["a6", "a9"],
    "b5": ["a1", "a5", "a9"],
    "b6": ["a4", "a8", "a10"],
    "b7": ["a3", "a4", "a6"],
    "b8": ["a1", "a8"],
    "b9": ["a3", "a4", "a6", "a7", "a10"],
}

graph = build_graph(mechanisms, jobs)
colors = greedy_coloring(graph)
schedule = make_schedule(colors)

print("Граф конфликтов:")
for job in jobs:
    print(job, sorted(graph[job], key=job_num))

print("Цвета:", colors)

print("Расписание:")
for color in sorted(schedule):
    print(color, sorted(schedule[color], key=job_num))

work_time = 1
total_time = max(colors.values()) * work_time

print("Общее время:", total_time)
print("Сложность: O(m * n^2 + n^2), где n - количество работ, m - количество механизмов")
