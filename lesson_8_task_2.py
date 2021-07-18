"""2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список
вершин, которые необходимо обойти."""

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float("inf")] * length
    parent = [-1] * len(graph)
    cost[start] = 0
    min_cost = 0

    vertexes = [[] for _ in range(length)]
    vertexes[start].append(start)

    while min_cost < float("inf"):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    vertexes[i].clear()
                    vertexes[i].extend(vertexes[start])
                    vertexes[i].append(i)




        min_cost = float("inf")

        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for row in range(len(vertexes)):
        if vertexes[row] == []:
            vertexes[row] = " Нет пути"

    return cost, vertexes


s = int(input("От какой вершины идти: "))
list_list = dijkstra(g, s)
print(f"Расстояние до вершин: {list_list[0]}")
print("Список вершин, которые необходимо обойти:", *list_list[1], sep = '\n')