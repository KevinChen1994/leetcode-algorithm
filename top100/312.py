# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/6 20:21
'''
solution: 动态规划。要找的就是一个点k，k将nums分割成两个list，k是最后戳破的，所以这是将问题分解为求nums[i,k-1]和nums[k+1,j]的最大值加上nums[i-1]*nums[k]*nums[j+1]的最大值。
要求的list可以表示为： [i-1, i, i+1, ..., k-1, k, k+1, ..., j-1, j, j+1]，所以目的就是求最合适的k。
'''
class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        nums = [1] + nums + [1]
        # dp[i][j]代表从i到j的最大值
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
        # 因为要求从i到j的最大值，所以要从短的list开始计算，l就是list的长度
        for l in range(1, n + 1):
            # list的起始位置，从1开始到n减去长度再加上1
            for i in range(1, n - l + 2):
                # j的大小是list的起始为位置i加上list的长度减去1
                j = i + l - 1
                # k的值就是从i到j
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1]+nums[i-1]*nums[k]*nums[j+1]+dp[k+1][j])
        return dp[1][n]


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 1, 5, 8]
    print(solution.maxCoins(nums))
