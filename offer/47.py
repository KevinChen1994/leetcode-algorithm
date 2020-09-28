# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/28 21:18

class Solution:
    def maxValue_1(self, grid) -> int:
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        dp = [[0] * m] * n
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                elif i == 0 and j != 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1]) + grid[i][j]
                elif i != 0 and j == 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j]) + grid[i][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

    def maxValue_2(self, grid):
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    grid[i][j] = max(grid[i][j], grid[i][j - 1] + grid[i][j])
                elif i != 0 and j == 0:
                    grid[i][j] = max(grid[i][j], grid[i - 1][j] + grid[i][j])
                else:
                    grid[i][j] = max(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        return grid[n - 1][m - 1]


if __name__ == '__main__':
    solution = Solution()
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(solution.maxValue_2(grid))
