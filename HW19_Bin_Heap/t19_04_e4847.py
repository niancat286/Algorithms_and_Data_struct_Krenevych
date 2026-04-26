class PriorityQueue:
    def __init__(self):
        self._items = []
        self._pos = {}

    def swap(self, i, j):
        id1 = self._items[i][1]
        id2 = self._items[j][1]

        self._pos[id1] = j
        self._pos[id2] = i

        self._items[i], self._items[j] = self._items[j], self._items[i]

    def siftUp(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self._items[parent][0] >= self._items[idx][0]:
                break
            self.swap(idx, parent)
            idx = parent

    def siftDown(self, idx):
        n = len(self._items)
        while 2 * idx + 1 < n:
            left = 2 * idx + 1
            right = 2 * idx + 2
            max_child = left

            if right < n and self._items[right][0] > self._items[left][0]:
                max_child = right

            if self._items[idx][0] >= self._items[max_child][0]:
                break

            self.swap(idx, max_child)
            idx = max_child

    def add(self, item_id, priority):
        self._items.append([priority, item_id])
        idx = len(self._items) - 1
        self._pos[item_id] = idx
        self.siftUp(idx)

    def pop(self):

        max_priority, max_id = self._items[0]
        self.swap(0, len(self._items) - 1)

        self._items.pop()
        del self._pos[max_id]

        if self._items:
            self.siftDown(0)

        return max_id, max_priority

    def change(self, item_id, new_priority):

        idx = self._pos[item_id]
        old_priority = self._items[idx][0]

        if old_priority == new_priority:
            return

        self._items[idx][0] = new_priority

        if new_priority > old_priority:
            self.siftUp(idx)
        else:
            self.siftDown(idx)


if __name__ == "__main__":
    pq = PriorityQueue()
    with open("input.txt") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            parts = line.split()
            cmd = parts[0]

            if cmd == "ADD":
                item_id = parts[1]
                priority = int(parts[2])
                pq.add(item_id, priority)

            elif cmd == "POP":
                max_id, max_priority = pq.pop()
                print(f"{max_id} {max_priority}")

            elif cmd == "CHANGE":
                item_id = parts[1]
                new_priority = int(parts[2])
                pq.change(item_id, new_priority)