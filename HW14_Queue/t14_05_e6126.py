

class Queue:

    def __init__(self, max_size = 100):
        self._front = 0
        self._back = 0
        self._size = 0
        self._max_size = max_size
        self._items = [None for _ in range(max_size)]

    def push(self, item):
        if self._size > 0:
            self._back = (self._back + 1) % self._max_size

        self._items[self._back] = item
        self._size += 1

        return "ok"

    def pop(self):
        if self._size == 0:
            return "error"
        item = self._items[self._front]
        self._items[self._front] = None
        self._size -= 1
        if self._size > 0:
            self._front = (self._front + 1) % self._max_size

        return item

    def front(self):
        if self._size == 0:
            return "error"
        return self._items[self._front]

    def size(self):
        return self._size

    def clear(self):
        self._front = self._back = self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    queue = Queue(100)
    with open("input.txt") as f:
        for line in f:
            result = queue.execute(line)
            print(result)

            if result == "bye":
                break