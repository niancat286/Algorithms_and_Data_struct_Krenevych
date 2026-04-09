import sys


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def AddToTail(self, val: int) -> None:
        """Додати число val у кінець зв'язаного списку"""
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def RotateRight(self, k: int) -> None:
        """Обернути список праворуч на k позицій"""
        if self.head is None or self.head.next is None or k == 0:
            return

        length = 1
        curr = self.head
        while curr.next:
            length += 1
            curr = curr.next

        k = k % length
        if k == 0:
            return

        iter = length - k
        new_tail = self.head

        for _ in range(iter - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        self.tail.next = self.head
        new_tail.next = None

        self.head = new_head
        self.tail = new_tail

    def Print(self) -> None:
        """Вивести елементи зв'язаного списку"""
        curr = self.head

        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next

        print()


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    my_list = List()

    for i in range(1, n + 1):
        my_list.AddToTail(int(input_data[i]))

    idx = n + 1
    while idx < len(input_data):
        k = int(input_data[idx])
        my_list.RotateRight(k)
        my_list.Print()
        idx += 1



if __name__ == "__main__":
    solve()