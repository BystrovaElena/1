# Определяем граф с весами рёбер
graph_example = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3, 'E': 1},
    'E': {'D': 1, 'A': 7}
}

# Функция для нахождения вершины с минимальным расстоянием
def min_distance_vertex(distances, vertices):
    min_distance = float('infinity')
    min_vertex = None
    for vertex in vertices:
        if distances[vertex] < min_distance:
            min_distance = distances[vertex]
            min_vertex = vertex
    return min_vertex

# Функция для нахождения кратчайшего пути и расстояния от начальной вершины до целевой
def find_shortest_path(graph, start, target):
    # Инициализируем расстояния как бесконечность
    distances = {vertex: float('infinity') for vertex in graph}
    # Расстояние до начальной вершины равно 0
    distances[start] = 0
    # Предшественники вершин для восстановления пути
    predecessors = {vertex: None for vertex in graph}
    # Множество всех вершин, которые ещё не были посещены
    pending_vertices = set(graph.keys())

    while pending_vertices:
        # Находим вершину с минимальным расстоянием
        current_vertex = min_distance_vertex(distances, pending_vertices)
        # Удаляем выбранную вершину из множества непосещённых
        pending_vertices.remove(current_vertex)

        # Если текущая вершина - целевая, прерываем цикл
        if current_vertex == target:
            break

        # Обновляем расстояния и предшественников для соседних вершин
        for neighbour, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            # Если найден более короткий путь, обновляем расстояние и предшественника
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                predecessors[neighbour] = current_vertex

    # Восстанавливаем кратчайший путь
    path = []
    current_vertex = target
    while current_vertex is not None:
        path.insert(0, current_vertex)
        current_vertex = predecessors[current_vertex]

    return distances[target], path

# Начальная и целевая вершины для поиска пути
starting_vertex = 'A'
target_vertex = 'D'
# Вызов функции и сохранение результата в переменные
shortest_distance, shortest_path = find_shortest_path(graph_example, starting_vertex, target_vertex)
# Вывод кратчайшего расстояния и пути от начальной до целевой вершины
print(f"Кратчайшее расстояние от вершины {starting_vertex} до вершины {target_vertex}: {shortest_distance}")
print(f"Кратчайший путь: {' -> '.join(shortest_path)}")