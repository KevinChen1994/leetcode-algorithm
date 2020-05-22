# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/22 16:19
'''
solution1: 这个方法解释的很清楚了，就是一个动态规划问题，也是背包问题。亮点在于，使用字典添加到数组中，代替了二维数组。但是速度并不快。
solution2:
这道题就是找一个子集是正数，剩下是负数，他们之和等于S
假设正数集和为P，负数集合为N，有
sum(P) - sum(N) = S
因为sum(nums) = sum(P) + sum(N)
那么有sum(P) - sum(N) + sum(P) + sum(N) = S + sum(nums)
有：2 * sum(P) = S + sum(nums)
sum(P) = (S + sum(nums))/2
那么就可以转换成一个背包问题。
花花酱的讲解：https://www.bilibili.com/video/BV1WW411C7Mr?from=search&seid=5509919470015937434
'''


class Solution:
    def findTargetSumWays_1(self, nums, S):
        """
        （1）思路：动态规划
                我们用 dp[i][j] 表示用数组中的前 i 个元素，组成和为 j 的方案数。考虑第 i 个数 nums[i]，它可以被添
            加 + 或 - ，那么从dp[i-1][m] —> dp[i][j] 可以在 dp[i-1][m]的基础上加上 nums[i] 或者减去 nums[i]，
            因此状态转移方程如下：
                dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j + nums[i]]
        （2）复杂度：
            - 时间复杂度：O（N * sums） 其中 N 是数组 nums 的长度
            - 空间复杂度：O（N * sums）
        """
        import collections
        # 获取数组长度和数组和的最大值
        array_length, max_sum = len(nums), sum(nums)
        # 定义和初始化dp数组
        # 因为该数组所能组成的值的区间为[min_sum, max_sum]，即一共有 max_sum - min_sum + 1 种值
        # 但是为了方便，可以直接定义为dict的形式，这样就可以一直增加key而不需要去计算dp数组第二维的长度，同时不用管下标为
        # 负数的情况，直接将下标转化为dict中的key
        # 这样不存在的key，也会默认是0
        dp = [collections.defaultdict(int) for _ in range(len(nums))]
        # 之所以dp[0][-nums[0]] 使用 += 1 而不是直接赋值1，是为了处理nums[0]就等于0的情况
        # 如果nums[0]， 那么dp[0][0] = 2 而不是 1
        dp[0][nums[0]] = 1
        dp[0][-nums[0]] += 1
        # 遍历nums数组，更行dp数组的值
        for i in range(1, array_length):
            for j in range(-max_sum, max_sum + 1):
                # 状态转移方程
                # 当dp[i][j]不等于的0的时候，代表至少存在一种方法得到j值
                dp[i][j] = dp[i - 1].get(j + nums[i], 0) + dp[i - 1].get(j - nums[i], 0)
        return dp[-1][S]

    def findTargetSumWays_2(self, nums, S):
        target = S + sum(nums)
        if sum(nums) < S or target < 0 or target % 2: return 0
        target //= 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(target, num - 1, -1):
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 1, 1, 1]
    S = 3
    print(solution.findTargetSumWays_2(nums, S))
