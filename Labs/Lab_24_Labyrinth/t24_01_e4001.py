from collections import deque

WALL = "*"
CELL = "."

VISITED = 1
EMPTY = 0



class Maze:

    def __init__(self, maze):
        self.maze = maze
        self.n = len(
            maze
        )
        self.directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def bfs_count_area(self, si, sj):
        wave_matrix = [[EMPTY]*self.n for _ in range(self.n)]

        queue = deque()
        queue.append((si, sj))
        wave_matrix[si][sj] = VISITED
        count = 0

        while queue:
            i,j = queue.popleft()
            count += 1
            for di, dj in self.directions:
                ni = i + di
                nj = j + dj

                if self.maze[ni][nj] == CELL and wave_matrix[ni][nj] == EMPTY:
                    queue.append((ni, nj))
                    wave_matrix[ni][nj] = VISITED

        return count


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        maze_matrix = [
            list(f.readline()) for _ in range(n)
        ]

        si, sj = map(lambda x: int(x) - 1, f.readline().split())

        maze = Maze(maze_matrix)
        print(maze.bfs_count_area(si, sj))
