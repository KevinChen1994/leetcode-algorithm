# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/11 18:19
# software: PyCharm
'''
solution1: 不占用额外空间的动态规划。
solution2: 占用额外空间的动态规划。
'''


class Solution:
    def minPathSum_1(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

    def minPathSum_2(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    # grid = [
    #     [1, 3, 1],
    #     [1, 5, 1],
    #     [4, 2, 1]
    # ]
    grid = [
        [1, 2, 3],
        [3, 2, 1]
    ]
    print(solution.minPathSum_2(grid))
