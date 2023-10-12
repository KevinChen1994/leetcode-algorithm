# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/27 22:28
from typing import List
'''
solution: 这道题看上去可能会复杂一点，其实就是一个求面积的变型。
首先需要求出各个岛屿的面积，这里需要将每块面积分配一个key值，同时在grid上将1修改成key值，
以便后边将0变成1的时候判断它挨着的是哪个面积。
最后重新遍历一遍grid,找到所有的0，然后逐一去判断如果将0改成1，它相邻的几个面积相加哪个最大。
'''

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        result = 0
        area_dict = {}
        # 因为grid是由0和1构成的，那么key就由2开始，这样不会混乱
        area_key = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area_dict[area_key] = self.dfs(grid, i, j, m, n, area_key)
                    result = max(result, area_dict[area_key])
                    area_key += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    area = 1
                    # 可能0周围的面积都是连通的，那么key也就是重复的，需要去重
                    key_list = set([self.get_key(grid, i - 1, j, m, n), self.get_key(grid, i + 1, j, m, n),
                                    self.get_key(grid, i, j - 1, m, n), self.get_key(grid, i, j + 1, m, n)])
                    for key in key_list:
                        if key in area_dict:
                            area += area_dict[key]
                    result = max(result, area)

        return result

    def dfs(self, grid, i, j, m, n, area_key):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or grid[i][j] == area_key:
            return 0
        grid[i][j] = area_key
        return self.dfs(grid, i - 1, j, m, n, area_key) + \
               self.dfs(grid, i + 1, j, m, n, area_key) + \
               self.dfs(grid, i, j - 1, m, n, area_key) + \
               self.dfs(grid, i, j + 1, m, n, area_key) + 1

    # 获取到当前0上下左右相邻的面积的key。
    def get_key(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n:
            return 0
        else:
            return grid[i][j]


if __name__ == '__main__':
    solution = Solution()
    grid = [
        [1, 1],
        [1, 0]
    ]
    print(solution.largestIsland(grid))
