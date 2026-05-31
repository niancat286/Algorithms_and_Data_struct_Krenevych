import sys
from math import inf
INF = sys.maxsize

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
        self.mElementsMap[key] = self.mSize  # S

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

    def __str__(self):
        res = ""
        for i in range(1, self.mSize + 1):
            res += str(self.mItems[i]) + "\n"
        return res


def getDistance(start, end, n, matrix): #алгоритм дейкстри
    distances = [inf] * n
    distances[start] = 0

    queue = PriorityQueue()
    queue.insert(start, 0)

    while not queue.empty():
        i = queue.extractMinimum()

        if i == end:
            break

        for j in range(n):
            weight = matrix[i][j]

            if weight != -1 and i != j:
                new_dist = distances[i] + weight

                if new_dist < distances[j]:
                    distances[j] = new_dist

                    if j not in queue:
                        queue.insert(j, distances[j])
                    else:
                        queue.updatePriority(j, distances[j])

    if distances[end] == inf:
        return -1
    else:
        return distances[end]


if __name__ == "__main__":
    with open("input.txt") as f:
        n, s, finish = map(int, f.readline().split())

        s -= 1
        finish -= 1

        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            matrix.append(row)

    print(getDistance(s, finish, n, matrix))
