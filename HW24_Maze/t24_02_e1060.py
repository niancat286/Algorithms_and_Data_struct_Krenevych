from collections import deque

WALL = "*"
CELL = "."

VISITED = 1
EMPTY = 0



class Maze:

    def __init__(self, maze):
        self.maze = maze
        self.n = len(maze)
        self.directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def bfs_find_path(self, si, sj):

        queue = deque([(si, sj, [])])   #here in [] i'll save the path
        visited = {(si, sj)}

        while queue:
            i,j,path = queue.popleft()
            if self.maze[i][j] =='X':   #if found the finish
                for pi, pj in path:    #draw + in all saved cells
                    self.maze[pi][pj] = "+"
                return True

            for di, dj in self.directions:
                ni = i + di
                nj = j + dj

                if (0 <= ni < self.n) and (0 <=nj < self.n) and ((ni, nj) not in visited):
                    if self.maze[ni][nj] in ('.', 'X'):
                        visited.add((ni, nj))
                        queue.append((ni, nj, path + [(ni, nj)]))

        return False





if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        maze_matrix = []
        si, sj = -1, -1

        for i in range(n):
            #print('hello1')
            row = list(f.readline().strip())
            maze_matrix.append(row)
            for j in range(n):
                #and where are you if not here
                if row[j] == '@':
                    si, sj = i, j

        maze = Maze(maze_matrix)
        if maze.bfs_find_path(si, sj):
            print('Y')
            for row in maze.maze:
                print("".join(row))
        else:
            print('N')
