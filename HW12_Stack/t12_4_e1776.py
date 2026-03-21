import sys


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:

    def __init__(self):
        self._top = None
        self._size = 0

    def empty(self):
        return self._top is None

    def push(self, item):
        node = Node(item)
        node.next = self._top
        self._top = node
        self._size += 1
        return "ok"

    def pop(self):
        if self.empty():
            return "error"

        item = self._top.item
        node = self._top
        self._top = node.next
        self._size -= 1

        return item

    def back(self):
        if self.empty():
            return "error"

        return self._top.item

    def size(self):
        return self._size

    def clear(self):
        self.__init__()



def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1

        if n == 0:
            break

        while idx < len(input_data):
            val1 = int(input_data[idx])

            if val1 == 0:
                idx += 1
                print()
                break

            target = [val1]
            for _ in range(1, n):
                idx += 1
                target.append(int(input_data[idx]))
            idx += 1

            s = Stack()
            cur = 1
            res = True

            for expected in target:
                while cur <= expected:
                    s.push(cur)
                    cur += 1

                if not s.empty() and s.back() == expected:
                    s.pop()
                else:
                    res = False
                    break

            if res:
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    solve()