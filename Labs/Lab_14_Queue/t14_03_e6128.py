

class Dequeue:

    def __init__(self, max_size = 100):
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
        item = self._items[self._front]
        self._items[self._front] = None
        self._size -= 1
        if self._size > 0 :
            self._front = (self._front + 1) % self.max_size

        return item

    def pop_back(self):
        item = self._items[self._back]
        self._items[self._back] = None
        self._size -= 1
        if self._size > 0 :
            self._back = (self._back - 1) % self.max_size

        return item

    def front(self):
        return self._items[self._front]

    def back(self):
        return self._items[self._back]

    def size(self):
        return self._size

    def clear(self):
        self.__init__(self.max_size)
        return "ok"

    @staticmethod
    def exit():
        return "bye"


    def execute(self,command: str):
        method, *args = command.split()
        return getattr(self,method)(*args)


if __name__ == "__main__":
    dequeue = Dequeue(100)
    with open("input.txt") as f:
        for line in f:
            result = dequeue.execute(line)
            print(result)
            if result == "bye":
                break

    # dequeue.push_back(3)
    # print(dequeue._items,dequeue._front,dequeue._back)
    # dequeue.push_back(5)
    # print(dequeue._items, dequeue._front, dequeue._back)
    # dequeue.push_front(7)
    # print(dequeue._items, dequeue._front, dequeue._back)
    # dequeue.push_front(6)
    # print(dequeue._items, dequeue._front, dequeue._back)
    # dequeue.push_front(4)
    # print(dequeue._items, dequeue._front, dequeue._back)
    # dequeue.pop_back()
    # print(dequeue._items, dequeue._front, dequeue._back)
    # dequeue.pop_back()
    # print(dequeue._items, dequeue._front, dequeue._back)
    # dequeue.pop_front()
    # print(dequeue._items, dequeue._front, dequeue._back)
    # dequeue.pop_front()
    # print(dequeue._items, dequeue._front, dequeue._back)
    # dequeue.pop_front()
    # print(dequeue._items, dequeue._front, dequeue._back)
