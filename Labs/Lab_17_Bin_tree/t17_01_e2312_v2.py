
class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        node = self
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = BinarySearchTree(key)
                    return
                else:
                    node = node.left

            elif key > node.key:
                if node.right is None:
                    node.right = BinarySearchTree(key)
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


    def height(self) -> int:
        max_height = 0

        stack = [(self, 1)]
        while stack:
            node, height = stack.pop()
            if height > max_height:
                max_height = height

            if node.left is not None:
                stack.append((node.left, height + 1))

            if node.right is not None:
                stack.append((node.right, height + 1))

        return max_height



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
