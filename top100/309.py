# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/5 23:12
'''
solution: 动态规划。首先需要定义几种状态：0，本来就不持有股票；1，持有股票；2，因为当天买入又卖出了所以不持有股票，收益为0。
然后初始化状态矩阵dp[0][0] = 0，dp[0][1] = -prices[0]，dp[0][2] = 0。状态矩阵如何进行转移，需要考虑以下问题。
第i天不持有股票，那么最大的收益应该为1：第i-1天就不持有股票；2：第i-1天不持有股票，第i天买入又卖出了。那么dp[i][0] = max(dp[i-1][0], dp[i-1][2])
第i天持有股票，那么最大的收益应该为1：第i-1天就持有股票；2：第i-1不持有股票，第i天买入。dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
第i天不持有股票，当天卖出，那么最大的收益应该为第i-1天持有股票，第i天卖出。dp[i][2] = dp[i-1][1] + prices[i]
最终最大的收益肯定是不持有股票的收益，对比不持有的两种状态就好。
这道题不用太关注冷冻期，因为在考虑状态转移的时候就把这个冷冻期考虑进去了，例如：i-1天卖出了，那么在计算第i天的时候，在买入这个状态下，除非i-1的状态是0也就是不持有才可以，
并不考虑2刚卖出的状态。
'''
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1: return 0
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
            dp[i][2] = dp[i-1][1] + prices[i]

        return max(dp[n-1][0], dp[n-1][2])


if __name__ == '__main__':
    solution = Solution()
    prices = [1, 2, 3, 0, 2]
    print(solution.maxProfit(prices))
