

class Stack:

    def __init__(self, max_size = 100):
        self._items = [0 for _ in range(max_size)]
        self._top = -1
        self._size = max_size

    def reloc(self):
        #print("reloc active")
        self._size *= 2
        self.new_container = [0] * self._size
        for i in range(len(self._items)):
            self.new_container[i] = self._items[i]

        self._items = self.new_container
    def push(self, item):
        if self._top == self._size - 1:
            self.reloc()
        self._top += 1
        self._items[self._top] = item
        return "ok"

    def pop(self):
        item = self._items[self._top]
        self._items[self._top] = 0
        self._top -= 1
        return item

    def back(self):
        return self._items[self._top]

    def size(self):
        return self._top + 1

    def clear(self):
        self.__init__(self._size)
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command: str):
        method, *args = command.split()
        func = getattr(self, method)
        return func(*args)


if __name__ == "__main__":
    with open("input.txt") as f:
        stack = Stack(10)

        for line in f:
            res = stack.execute(line)
            print(res)
            if res == "bye":
                break

