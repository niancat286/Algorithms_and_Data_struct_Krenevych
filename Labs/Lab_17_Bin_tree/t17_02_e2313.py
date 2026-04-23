
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


    def count_bfs(self) -> int:
        count = 0

        stack = [self]
        while stack:
            node = stack.pop()
            count += 1

            if node.left is not None:
                stack.append(node.left)

            if node.right is not None:
                stack.append(node.right)

        return count



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
            #print(tree.count_bfs())
            print(tree.count_bfs() == tree.size)
        else:
            print(0)
