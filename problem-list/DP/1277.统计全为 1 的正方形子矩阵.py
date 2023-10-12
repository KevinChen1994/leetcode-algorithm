# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/22 18:27
from typing import List
'''
solution: 乍一看求正方形个数有点懵逼，经过手动计算得出结论，其实求出正方形边长就知道这个区域有多少个正方形了，
那就把这个问题转换为求正方形边长的问题，跟221.maximal-square就很像了。
'''

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        res = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = matrix[i][j]
                if i != 0 and j != 0 and dp[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                res += dp[i][j]
        return res


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]
    print(solution.countSquares(matrix))
