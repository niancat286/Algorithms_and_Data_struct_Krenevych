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

    def pre_print(self):
        print(self.key, end='')

        if self.left is not None:
            self.left.pre_print()

        if self.right is not None:
            self.right.pre_print()


def solve():
    lst = []

    with open("input.txt") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line == '*':
                break

            lst.append(line)

    full_lst = "".join(lst)

    if not full_lst:
        print()
        return

    rev_full_lst = full_lst[::-1]

    tree = BinarySearchTree(rev_full_lst[0])

    for i in range(1, len(rev_full_lst)):
        tree.insert(rev_full_lst[i])

    tree.pre_print()
    print()


if __name__ == "__main__":
    solve()