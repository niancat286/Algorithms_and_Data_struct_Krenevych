"""
Нехай задано орієнтований зважений граф.
Знайдіть найкоротший шляху між двома заданими вузлами цього графа
"""
from math import inf
from PriorityQueue import PriorityQueue

graph: list[dict]
n: int

def init(vertices, edges):
    """ Ініціалізація графа.

    Викликається один раз на початку виконання програми.
    @param vertices: кількість вершин графа
    @param edges:  кількість ребер графа
    """
    global graph, n
    n = vertices
    graph = [{} for _ in range(n)]


def addEdge(source, destination, weight):
    """ Додає зважене ребро графа

    @param source: вершини з якої виходить ребро
    @param destination: вершина у яку входить ребро
    @param weight: вага ребра
    """
    graph[source][destination] = weight


def getWay(start, end): #дейкстра
    """ Знаходить найкоротший шлях, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: список вершин шляху або порожній список, якщо шляху між вершинами не існує.
    """
    distances = [inf] * n
    distances[start] = 0
    source = [-1] * n

    queue = PriorityQueue()
    queue.insert(start, 0)

    while not queue.empty():
        i = queue.extractMinimum()

        if i == end:
            break

        for j in graph[i]:
            new_dist = distances[i] + graph[i][j]
            if new_dist < distances[j]:
                distances[j] = new_dist
                source[j] = i

                if j not in queue:
                    queue.insert(j, distances[j])
                else:
                    queue.updatePriority(j, distances[j])

    else:
        return []

    path = []
    i = end
    while i != -1:
        path.append(i)
        i = source[i]

    path.reverse()
    return path



if __name__ == "__main__":
    init(7, 0)
    addEdge(1, 2, 8)
    addEdge(1, 3, 7)
    addEdge(1, 4, 2)
    addEdge(1, 5, 1)
    addEdge(2, 6, 5)
    addEdge(2, 5, 2)
    addEdge(3, 4, 3)
    addEdge(4, 3, 3)
    addEdge(4, 5, 4)
    addEdge(5, 2, 2)
    addEdge(5, 6, 10)
    #print(graph)
    print(getWay(1, 6))
