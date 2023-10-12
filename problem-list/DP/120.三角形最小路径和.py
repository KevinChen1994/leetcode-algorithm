# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/22 10:27
from typing import List
'''
solution: 在每一个位置下，考虑哪里可以到这，使用最短的路径到这就可以了。
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        if m == 0:
            return 0
        dp = [[0 for _ in range(m)] for _ in range(m)]
        for i in range(m):
            for j in range(i + 1):
                if i == j == 0:
                    dp[i][j] = triangle[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif i == j:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        return min(dp[-1])

if __name__ == '__main__':
    solution = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(solution.minimumTotal(triangle))