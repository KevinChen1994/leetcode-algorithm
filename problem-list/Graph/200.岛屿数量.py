# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/27 16:31
from typing import List
'''
solution1: 比较容易理解的方法，设置一个辅助矩阵，形状跟grid相同，初始值为False。
如果当前位置为1，那么这里就是一块陆地，需要找到他周边相邻的所有1，利用队列来进行判断，这里也是利用了dfs的思想，
通过当前位置的上下左右四个方向分别判断，遇到相邻的1，就将辅助矩阵对应的位置设置为True。
solution2: 直接使用dfs进行递归，在原grid上进行修改，空间复杂度会低点。
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        result = 0
        marked = [[False for _ in range(n)] for _ in range(m)]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and marked[i][j] is False:
                    marked[i][j] = True
                    result += 1
                    queue = []
                    queue.append((i, j))
                    while queue:
                        cur_i, cur_j = queue.pop(0)
                        for direction in directions:
                            new_i = cur_i + direction[0]
                            new_j = cur_j + direction[1]
                            if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == '1' and marked[new_i][
                                new_j] is False:
                                marked[new_i][new_j] = True
                                queue.append((new_i, new_j))
        return result

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result += 1
                    self.dfs(grid, i, j, m, n)
        return result

    def dfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i - 1, j, m, n)
        self.dfs(grid, i + 1, j, m, n)
        self.dfs(grid, i, j - 1, m, n)
        self.dfs(grid, i, j + 1, m, n)


if __name__ == '__main__':
    solution = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(solution.numIslands(grid))
