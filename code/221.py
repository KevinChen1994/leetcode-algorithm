# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/20 22:57
'''
solution1: 动态规划
'''
class Solution:
    def maximalSquare(self, matrix):
        rows = len(matrix)
        if rows == 0: return 0
        cols = len(matrix[0])
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        maxlen = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    maxlen = max(maxlen, dp[i][j])
        return maxlen * maxlen


if __name__ == '__main__':
    solution = Solution()
    # matrix = [["1", "0", "1", "0", "0"],
    #           ["1", "0", "1", "1", "1"],
    #           ["1", "1", "1", "1", "1"],
    #           ["1", "0", "0", "1", "0"]]
    matrix = [['1']]
    print(solution.maximalSquare(matrix))
