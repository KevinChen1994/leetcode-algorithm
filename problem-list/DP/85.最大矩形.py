# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/22 15:51
from typing import List

'''
solution: 这里使用的是花花酱的解答，相对比较容易理解，更fancy的解法在top100-85里有写，这里不重复了。
dp[i][j]代表第i行第j列最大的宽度，首先求出所有位置最大的宽度，然后求出每个位置下最小的宽度，用高度乘宽度就是面积。
'''


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        res = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 if j == 0 else dp[i][j - 1] + 1
                else:
                    dp[i][j] = 0
        for i in range(m):
            for j in range(n):
                width = float('inf')
                for k in range(i, m):
                    width = min(width, dp[k][j])
                    if width == 0:
                        break
                    res = max(res, width * (k - i + 1))
        return res


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(solution.maximalRectangle(matrix))
