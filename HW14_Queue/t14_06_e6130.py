class Dequeue:

    def __init__(self, max_size = 100005):
        self.max_size = max_size
        self._size = 0
        self._front = 0
        self._back = 0
        self._items = [None for _ in range(max_size)]


    def push_back(self, item):
        if self._size > 0:
            self._back = (self._back + 1) % self.max_size
        self._items[self._back] = item
        self._size += 1

        return "ok"

    def push_front(self,item):
        if self._size > 0:
            self._front = (self._front - 1) % self.max_size
        self._items[self._front] = item
        self._size += 1

        return "ok"


    def pop_front(self):
        if self._size == 0:
            return "error"
        item = self._items[self._front]
        self._items[self._front] = None
        self._size -= 1
        if self._size > 0 :
            self._front = (self._front + 1) % self.max_size

        return item

    def pop_back(self):
        if self._size == 0:
            return "error"
        item = self._items[self._back]
        self._items[self._back] = None
        self._size -= 1
        if self._size > 0 :
            self._back = (self._back - 1) % self.max_size

        return item

    def front(self):
        if self._size == 0:
            return "error"
        return self._items[self._front]

    def back(self):
        if self._size == 0:
            return "error"
        return self._items[self._back]

    def size(self):
        return self._size

    def clear(self):
        self._size = 0
        self._front = 0
        self._back = 0
        return "ok"

    @staticmethod
    def exit():
        return "bye"


    def execute(self,command: str):
        method, *args = command.split()
        return getattr(self,method)(*args)


if __name__ == "__main__":
    dequeue = Dequeue()
    with open("input.txt") as f:
        for line in f:
            result = dequeue.execute(line)
            print(result)
            if result == "bye":
                break
