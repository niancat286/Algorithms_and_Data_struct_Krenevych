

class Queue:

    def __init__(self, max_size = 100):
        self.max_size = max_size
        self._size = 0
        self._front = 0
        self._back = 0
        self._items = [None for _ in range(max_size)]


    def push(self,item):
        if self._size > 0:
            self._back = (self._back + 1) % self.max_size
        self._items[self._back] = item
        self._size += 1

        return "ok"

    def pop(self)-> int:
        item = self._items[self._front]
        self._items[self._front] = None
        self._size -= 1
        if self._size > 0 :
            self._front = (self._front + 1) % self.max_size

        return item


def solve(N: int, k: int) -> int:

    queue =  Queue(N)
    for i in range(1,N + 1):
        queue.push(i)
    # print(queue._items, queue._front, queue._back)
    while queue._size > 1:

        for _ in range(k - 1):
            queue.push(queue.pop())
            # print(queue._items, queue._front, queue._back)
        queue.pop()

        # print(queue._items,queue._front,queue._back)

    return queue.pop()


if __name__ == "__main__":
    N,k = map(int,input().split())
    print(solve(N,k))
