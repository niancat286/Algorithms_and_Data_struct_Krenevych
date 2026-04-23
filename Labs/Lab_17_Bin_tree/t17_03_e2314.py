
class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1

    def insert(self, key):
        node = self
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = BinarySearchTree(key)
                    self.size += 1
                    return
                else:
                    node = node.left

            elif key > node.key:
                if node.right is None:
                    node.right = BinarySearchTree(key)
                    self.size += 1
                    return

                else:
                    node = node.right

            else:
                break

    def print(self):

        if self.left is not None:
            self.left.print()


        if self.right is not None:
            self.right.print()

        print(self.key, end=' ')

    def second_maximum(self) -> int:
        parent = self
        node = self
        while node.right is not None:
            parent = node
            node = node.right

        if node.left is None:
            return parent.key

        node = node.left
        while node.right is not None:
            node = node.right

        return node.key



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
            print(tree.second_maximum())
            #print(tree.count_bfs() == tree.size)
        else:
            print(0)
