# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/27 17:46
from typing import List
'''
solution: 使用dfs找到相连的岛屿并记录下面积
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result = max(result, self.dfs(grid, i, j, m, n))
        return result

    def dfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        return self.dfs(grid, i - 1, j, m, n) + \
               self.dfs(grid, i + 1, j, m, n) + \
               self.dfs(grid, i, j - 1, m, n) + \
               self.dfs(grid, i, j + 1, m, n) + 1


if __name__ == '__main__':
    solution = Solution()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(solution.maxAreaOfIsland(grid))
