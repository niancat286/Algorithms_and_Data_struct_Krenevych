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

    def size(self):
        return self._size


def solve():
    player1 = None
    player2 = None
    n = 0
    line_num = 0

    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line_num == 0:
                n = int(line)
                player1 = Dequeue(n + 5)
                player2 = Dequeue(n + 5)

            elif line_num == 1:
                for card in line.split():
                    player1.push_back(int(card))

            elif line_num == 2:
                for card in line.split():
                    player2.push_back(int(card))

            line_num += 1

    if player1 is None or player2 is None:
        return

    moves = 0
    limit = 200000

    while player1.size() > 0 and player2.size() > 0:
        if moves >= limit:
            print("draw")
            return

        card1 = player1.pop_front()
        card2 = player2.pop_front()

        if card1 == 0 and card2 == n - 1:
            winner = 1
        elif card1 == n - 1 and card2 == 0:
            winner = 2
        elif card1 > card2:
            winner = 1
        else:
            winner = 2

        if winner == 1:
            player1.push_back(card1)
            player1.push_back(card2)
        else:
            player2.push_back(card1)
            player2.push_back(card2)

        moves += 1

    if player1.size() == 0:
        print(f"second {moves}")
    else:
        print(f"first {moves}")



if __name__ == "__main__":
    solve()
