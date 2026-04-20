import sys


class DirTree:
    def __init__(self):
        self.children: dict[str, 'DirTree'] = {}

    def add_path(self, path_piece: list[str]):
        curr = self

        for fold in path_piece:
            if fold not in curr.children:
                curr.children[fold] = DirTree()

            curr = curr.children[fold]

    def print_tree(self, depth: int = 0):
        for folder_name in sorted(self.children.keys()):
            print(" " * depth + folder_name)
            self.children[folder_name].print_tree(depth + 1)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    root = DirTree()

    for i in range(1, n + 1):
        path = input_data[i]
        # for instance: "WINNT\SYSTEM32" -> ["WINNT", "SYSTEM32"]
        folders = path.split('\\')

        root.add_path(folders)

    root.print_tree(0)


if __name__ == "__main__":
    solve()





