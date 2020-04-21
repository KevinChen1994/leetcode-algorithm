# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/20 22:57
'''
solution1: 动态规划。通过转移矩阵记录当前位置最大的边长，边长的计算方式为min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
意思就是取当前位置的上，斜上，左的最小长度加1。
solution2: 优化的动态规划。使用一维数组进行记录状态。其中dp[j-1]代表当前元素的左边那个元素的状态，dp[i]代表当前元素上边元素的状态，prev代表当前元素左上角元素状态。
prev比较不好理解，prev保存的是与当前元素同一列的上方元素的值。
'''


class Solution:
    def maximalSquare_1(self, matrix):
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

    def maximalSquare_2(self, matrix):
        rows = len(matrix)
        if rows == 0: return 0
        cols = len(matrix[0])
        dp = [0 for _ in range(cols + 1)]
        maxlen = 0
        prev = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j - 1], prev, dp[j]) + 1
                    maxlen = max(maxlen, dp[j])
                else:
                    # 因为DP数组为一维，所以如果是0需要将数组状态置为0，否则会影响下一行的判断
                    dp[j] = 0
                # prev代表的是本轮当前DP数组上一个的值，在下一轮使用的时候就是代表的当前的左上角那个元素的状态。
                prev = temp
        return maxlen * maxlen


if __name__ == '__main__':
    solution = Solution()
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    # matrix = [['1']]
    matrix = [["1", "0", "1", "1", "1"],
              ["0", "1", "0", "1", "0"],
              ["1", "1", "0", "1", "1"],
              ["1", "1", "0", "1", "1"],
              ["0", "1", "1", "1", "1"]]
    print(solution.maximalSquare_2(matrix))
