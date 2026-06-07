class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Dequeue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def push_front(self, item):
        new_node = Node(item)
        if self._size == 0:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

        self._size += 1
        return "ok"

    def push_back(self, item):
        new_node = Node(item)
        if self._size == 0:
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1
        return "ok"

    def pop_front(self):
        if self._size == 0:
            return "error"

        item = self._head.value
        self._head = self._head.next
        self._size -= 1

        if self._size == 0:
            self._tail = None
        else:
            self._head.prev = None

        return item

    def pop_back(self):
        if self._size == 0:
            return "error"

        item = self._tail.value
        self._tail = self._tail.prev
        self._size -= 1

        if self._size == 0:
            self._head = None
        else:
            self._tail.next = None

        return item

    def front(self):
        if self._size == 0:
            return "error"
        return self._head.value

    def back(self):
        if self._size == 0:
            return "error"
        return self._tail.value

    def size(self):
        return self._size

    def clear(self):
        self._head = None
        self._tail = None
        self._size = 0
        return "ok"

    @staticmethod
    def exit():
        return "bye"

    def execute(self, command: str):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    dequeue = Dequeue()
    with open("input.txt") as f:
        for line in f:
            if not line.strip():
                continue

            result = dequeue.execute(line.strip())
            print(result)

            if result == "bye":
                break