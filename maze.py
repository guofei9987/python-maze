import numpy as np


class Maze:
    def __init__(self, maze, point):
        # 每次只能上下左右试探
        self.step_set = np.array([[1, 0],
                                  [-1, 0],
                                  [0, 1],
                                  [0, -1]])
        self.maze = maze
        self.length, self.width = maze.shape
        self.init_maze()
        self.maze = self.find_next_step(self.maze, point)

    def init_maze(self):
        length, width = self.maze.shape
        maze_0 = np.zeros(shape=(length, width))
        maze_0[::2, ::2] = 1
        maze = np.where(self.maze < 0, self.maze, maze_0)
        self.maze = maze

    def find_next_step(self, maze, point):
        # 用递归实现深度优先搜索
        step_set = np.random.permutation(self.step_set)
        for next_step in step_set:
            next_point = point + next_step * 2
            x, y = next_point
            if 0 <= x < self.length and 0 <= y < self.width:  # 在格子内
                if maze[x, y] == 1:  # 如果还没打通，就打通
                    maze[x, y] = 2
                    maze[(point + next_step)[0], (point + next_step)[1]] = 2
                    maze = self.find_next_step(maze, next_point)  # 深度优先搜索
        # 全部遍历后，还是找不到，就是这个叶节点没有下一步了，返回即可
        return maze
