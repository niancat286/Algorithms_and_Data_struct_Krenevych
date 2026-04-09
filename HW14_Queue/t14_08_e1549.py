import sys


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

    def pop_front(self):
        if self._size == 0:
            return "error"
        item = self._items[self._front]
        self._items[self._front] = None
        self._size -= 1
        if self._size > 0 :
            self._front = (self._front + 1) % self.max_size

        return item

    def front(self):
        if self._size == 0:
            return "error"
        return self._items[self._front]

    def size(self):
        return self._size


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        k = int(input_data[idx + 2])
        idx += 3

        if n == 0 and m == 0 and k == 0:
            break

        q = Dequeue(n + m + 5)

            #let us name Blue as 0 and Red as 1

        for _ in range(n):
                q.push_back(0)
        for _ in range(m):
            q.push_back(1)

        while q.size() > 1:
            temp1 = (k - 1) % q.size()
            for _ in range(temp1):
                q.push_back(q.pop_front())
            p1 = q.pop_front()

            temp2 = (k - 1) % q.size()

            for _ in range(temp2):
                q.push_back(q.pop_front())
            p2 = q.pop_front()

            if p1 == p2:
                new_p = 0
            else:
                new_p = 1

            q.push_back(new_p)


        winner = q.front()
        if winner == 0:
            print("Gared")   #here is problem with translation, =Blue
        else:
            print("Keka")    #same, =Red


if __name__ == "__main__":
    solve()