# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/22 13:56
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                elif j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
                elif j == n - 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
        return min(dp[-1])


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [2, 1, 3],
        [6, 5, 4],
        [7, 8, 9]
    ]
    print(solution.minFallingPathSum(matrix))
