# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/29 22:45
'''
solution1: 动态规划。使用动态转移矩阵来记录每一个位置的最小平方数个数。转移矩阵的计算方法为 dp[i] = min(dp[i], dp[i-j*j]+1)
首先每一个位置的dp初始值都为当前索引的值，具体原因为如果当前这个位置的数没有符合的平方数，保底也有n个1相加，也就是当前位置的索引的值。
然后设置一个j，所谓j就是平方数在平方之前的值，从1开始，一直累加，知道当前值i-j*j < 0为止，这时在判断dp[i-j*j]+1与dp[i]的大小,
i-j*j就是当前值减去一个平方数，之后在动态规划这个过程。。。
'''
class Solution:
    def numSquares_1(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(n+1):
            dp[i] = i
            j = 1
            while i - j*j >= 0:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[n]

if __name__ == '__main__':
    solution = Solution()
    n = 13
    print(solution.numSquares_1(n))