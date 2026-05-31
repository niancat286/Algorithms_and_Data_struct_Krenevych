"""
Нехай задано орієнтований зважений граф.
Знайдіть довжину найкоротшого шляху між двома заданими вузлами цього графа
"""
from math import inf

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



def findDistance(start, end):   #белман-форд
    """ Знаходить довжину найкоротшого шляху, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: Довжину найкоротшого шляху або -1 якщо шляху між вершинами не існує.
    """
    distances = [inf] * n
    distances[start] = 0

    for _ in range(n-1):
        is_relaxed = True

        for i in range(n):
            for j in graph[i]:
                new_dist = distances[i] + graph[i][j]
                if new_dist < distances[j]:
                    distances[j] = new_dist
                    is_relaxed = False

            #print(distances)

        if is_relaxed:
            break

    if distances[end] == inf:
        return -1
    else:
        return distances[end]




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
    print(findDistance(1, 6))