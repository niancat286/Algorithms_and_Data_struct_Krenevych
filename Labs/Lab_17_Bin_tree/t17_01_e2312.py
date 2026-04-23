
import sys
sys.setrecursionlimit(100500)


class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = BinarySearchTree(key)
            else:
                self.left.insert(key)

        elif key > self.key:
            if self.right is None:
                self.right = BinarySearchTree(key)

            else:
                self.right.insert(key)

    def print(self):

        if self.left is not None:
            self.left.print()

        if self.right is not None:
            self.right.print()

        print(self.key, end=' ')

    def height(self) -> int:
        left_height = 0 if self.left is None else self.left.height()
        right_height = 0 if self.right is None else self.right.height()

        return max(left_height, right_height) + 1





if __name__ == "__main__":
    with open("input.txt") as f:
        lst = list(map(int, f.readline().split()))
        if lst[0] != 0:
            tree = BinarySearchTree(lst[0])

            for i in range(1, len(lst)):
                if lst[i] == 0:
                    break

                tree.insert(lst[i])

            #tree.print()
            print(tree.height())
        else:
            print(0)
