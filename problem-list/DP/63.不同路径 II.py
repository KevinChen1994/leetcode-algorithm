# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/21 22:16
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(solution.uniquePathsWithObstacles(obstacleGrid))
