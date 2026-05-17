
class Maze:

    def __init__(self, m, n, maze):
        self.m = m
        self.n = n
        self.maze = maze
        self.directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def _wave(self, si, sj):    #actually we need to check everything with dfs

        stack = [(si, sj)]

        self.maze[si][sj] = '.'

        while stack:
            i,j = stack.pop()
            for di, dj in self.directions:
                ni = i + di
                nj = j + dj

                if 0<=ni<self.m and 0<=nj<self.n:
                    if self.maze[ni][nj] == '#':
                        stack.append((ni, nj))
                        self.maze[ni][nj] = '.' #change every # into . in case not to visit it again

    def count_parts(self):
        count = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.maze[i][j] == '#':
                    count += 1
                    self._wave(i, j)

        return count




if __name__ == "__main__":
    with open("input.txt") as f:
        m, n = map(int, f.readline().split())

        maze_matrix = [
            list(f.readline()) for _ in range(m)
        ]



        maze = Maze(m, n, maze_matrix)
        print(maze.count_parts())
