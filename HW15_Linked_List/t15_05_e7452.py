import sys


class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None

class List:

    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None

    def addToTail(self, val: int) -> None:
        """Додати число val в кінець Зв'язного Списку"""
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        """Вивести елементи Зв'язного Списку"""
        curr = self.head

        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next

        print()

    def reverse(self, node: Node | None):
        if node is None:
            return
        self.reverse(node.next)
        print(node.data, end=" ")


    def PrintReverse(self) -> None:
        """Вивести елементи Зв'язного Списку в зворотному порядку"""
        self.reverse(self.head)
        print()


if __name__ == "__main__":
    input_data = sys.stdin.read().split()

    if input_data:
        n = int(input_data[0])
        my_list = List()

        for i in range(1, n + 1):
            my_list.addToTail(int(input_data[i]))

        my_list.Print()
        my_list.PrintReverse()