import sys

INF = float('inf')


class PQElement:
    def __init__(self, key=None, priority=INF):
        self.mKey = key
        self.mPriority = priority

    def updatePriority(self, priority):
        self.mPriority = priority

    def key(self):
        return self.mKey

    def __le__(self, other):
        return self.mPriority <= other.mPriority

    def __lt__(self, other):
        return self.mPriority < other.mPriority

    def __gt__(self, other):
        return self.mPriority > other.mPriority

    def __ge__(self, other):
        return self.mPriority >= other.mPriority

    def __str__(self):
        return "(item: {}, priority: {})".format(self.mKey, self.mPriority)


class PriorityQueue:
    def __init__(self):
        self.mItems = [PQElement(0, 0)]
        self.mSize = 0
        self.mElementsMap = {}

    def empty(self):
        return len(self.mItems) == 1

    def insert(self, key, priority):
        el = PQElement(key, priority)
        self.mSize += 1
        self.mItems.append(el)
        self.mElementsMap[key] = self.mSize
        self.siftUp()

    def extractMinimum(self):
        root = self.mItems[1].key()
        self.swap(1, -1)
        self.mItems.pop()
        del self.mElementsMap[root]
        self.mSize -= 1
        self.siftDown()
        return root

    def swap(self, i, j):
        pos_i = self.mItems[i].key()
        pos_j = self.mItems[j].key()
        self.mElementsMap[pos_i] = j
        self.mElementsMap[pos_j] = i
        self.mItems[i], self.mItems[j] = self.mItems[j], self.mItems[i]

    def siftDown(self):
        i = 1
        while (2 * i) <= self.mSize:
            left = 2 * i
            right = 2 * i + 1
            min_child = self.minChild(left, right)
            if self.mItems[i] > self.mItems[min_child]:
                self.swap(min_child, i)
            else:
                break
            i = min_child

    def siftUp(self):
        i = len(self.mItems) - 1
        while i > 1:
            parent = i // 2
            if self.mItems[i] < self.mItems[parent]:
                self.swap(parent, i)
            else:
                break
            i = parent

    def minChild(self, left_child, right_child):
        if right_child > self.mSize:
            return left_child
        else:
            if self.mItems[left_child] < self.mItems[right_child]:
                return left_child
            else:
                return right_child

    def __contains__(self, item):
        return item in self.mElementsMap

    def updatePriority(self, key, priority):
        i = self.mElementsMap[key]
        self.mItems[i].updatePriority(priority)
        while i > 1:
            parent = i // 2
            if self.mItems[i] < self.mItems[parent]:
                self.swap(parent, i)
            else:
                break
            i = parent
        return True


class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n + 1)]

    def add_edge(self, u, v, weight):
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def check_mst_edge(self, p, q):
        costs = [INF] * (self.n + 1)
        costs[1] = 0

        sources = [-1] * (self.n + 1)

        queue = PriorityQueue()
        queue.insert(1, 0)

        for j in range(2, self.n + 1):
            queue.insert(j, INF)

        while not queue.empty():
            u = queue.extractMinimum()

            for v, weight in self.adj[u]:
                if v in queue and costs[v] > weight:
                    costs[v] = weight
                    queue.updatePriority(v, costs[v])
                    sources[v] = u

        if sources[p] == q or sources[q] == p:
            return "YES"
        else:
            return "NO"


if __name__ == "__main__":
    with open("input.txt") as f:
        t = int(f.readline().strip())

        out = []

        for _ in range(t):
            n, m, p, q = map(int, f.readline().split())

            graph = Graph(n)

            for _ in range(m):
                u, v, w = map(int, f.readline().split())
                graph.add_edge(u, v, w)

            out.append(graph.check_mst_edge(p, q))

    print("\n".join(out))