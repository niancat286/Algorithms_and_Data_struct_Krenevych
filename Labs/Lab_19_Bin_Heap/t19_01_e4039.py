

class MaxHeap:
    def __init__(self):
        self._items = []

    def parent(self, idx):
        return (idx - 1) // 2

    def leftChind(self, idx):
        return 2*idx + 1

    def rightChind(self, idx):
        return 2*idx + 2

    def swap(self, idx1, idx2):
        self._items[idx1], self._items[idx2] = self._items[idx2], self._items[idx1]

    def insert(self, item):
        self._items.append(item)
        self.siftUp(len(self._items) - 1)

    def siftUp(self, idx):
        i = idx
        while i > 0:
            parent = self.parent(i)

            if self._items[parent] >= self._items[i]:
                break

            self.swap(i, parent)
            i = parent

    def siftDown(self, idx):
        i = idx
        while self.leftChind(i) < len(self._items):
            left = self.leftChind(i)
            right = self.rightChind(i)

            if right < len(self._items) and self._items[left] < self._items[right]:
                max_child = right

            else:
                max_child = left

            if self._items[max_child] <= self._items[i]:
                break

            self.swap(max_child, i)
            i = max_child


    def extract_maximum(self) -> int:
        self.swap(0, -1)
        item = self._items.pop()

        self.siftDown(0)


        return item


if __name__ == "__main__":
    heap = MaxHeap()
    with open("../../HW19_Bin_Heap/input.txt") as f:
        n = int(f.readline().strip())
        for i in range(n):
            cmd_id, *args = map(int, f.readline().split())
            if cmd_id == 0:
                heap.insert(*args)

            elif cmd_id == 1:
                print(heap.extract_maximum())