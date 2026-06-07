class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        if self._size == 0:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1
        return "ok"

    def pop(self):
        if self._size == 0:
            return "error"

        item = self._head.value
        self._head = self._head.next
        self._size -= 1

        if self._size == 0:
            self._tail = None

        return item

    def front(self):
        if self._size == 0:
            return "error"
        return self._head.value

    def size(self):
        return self._size

    def clear(self):
        self._head = None
        self._tail = None
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    queue = Queue()
    with open("input.txt") as f:
        for line in f:
            if not line.strip():
                continue
            result = queue.execute(line.strip())
            print(result)

            if result == "bye":
                break