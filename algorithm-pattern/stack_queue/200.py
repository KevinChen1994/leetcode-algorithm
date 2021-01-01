# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/15 09:42
'''
solution1: dfs，一直沿着一个方向找，直到遇到为0的点，会换个方向，然后再沿着一个方向找，直到把整个岛屿标记完。
solution2: bfs，借用队列实现，一个点先沿着他周边四个方向找，把周边的四个方向全部验证一遍，之后在到另外一个点，继续验证四个方向，直到把整个岛屿标记完。
'''
class Solution:
    def numIslands_1(self, grid):
        result = 0
        # 左、下、右、上
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        m = len(grid)
        if m == 0:
            return result
        n = len(grid[0])
        marked = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and marked[i][j] is False:
                    result += 1
                    self.dfs(i, j, m, n, marked, grid)
        return result

    def dfs(self, i, j, m, n, marked, grid):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == '1' and marked[new_i][new_j] is False:
                self.dfs(new_i, new_j, m, n, marked, grid)

    def numIslands_2(self, grid):
        from _collections import deque
        result = 0
        # 左、下、右、上
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        m = len(grid)
        if m == 0:
            return result
        n = len(grid[0])
        marked = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and marked[i][j] is False:
                    result += 1
                    queue = deque()
                    queue.appendleft((i, j))
                    while queue:
                        cur_i, cur_j = queue.pop()
                        for direction in directions:
                            new_i = cur_i + direction[0]
                            new_j = cur_j + direction[1]
                            if 0 <= new_i < m and 0 <= new_j < n and marked[new_i][new_j] is False and grid[new_i][
                                new_j] == '1':
                                marked[new_i][new_j] = True
                                queue.appendleft((new_i, new_j))
        return result


if __name__ == '__main__':
    solution = Solution()
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    print(solution.numIslands_2(grid))
