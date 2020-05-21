# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/15 15:29
'''
solution1: 二维数组动态规划。想象成背包问题，就是把nums数组和的一半作为target，当元素相加的和为target时，说明满足条件。状态转移矩阵：dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
dp[i][j]代表前i个数中，凑成的和是否为j，状态转移时需要参考上一行的状态，假设当前位置的上边是符合条件的，那么当前位置也是符合条件的，但是现在要考虑要不要加上当前这个数，
那么就考虑如果不加是不是符合条件：dp[i - 1][j]，或者加上是否符合条件：dp[i - 1][j - nums[i]]，这两个只要有一个符合条件就行。
solution2: 对solution1的优化，加了剪枝。
solution3: 一维数组动态规划。在转移矩阵初始化的时候没看太明白，不知道为什么dp[nums[0]]要设置为True。
'''


class Solution:
    def canPartition_1(self, nums):
        n = len(nums)
        if n == 0:
            return False
        sum = 0
        for num in nums:
            sum += num
        # 如果总和是奇数，返回False
        if sum % 2 != 0:
            return False
        target = sum // 2
        # dp[i][j]为前i个数中是否有能够凑成和为j的数
        dp = [[False for _ in range(target + 1)] for _ in range(n)]
        # 先填表格第 0 行，第 1 个数只能让容积为它自己的背包恰好装满（没看懂啥意思，去掉也能AC）
        if nums[0] == target:
            dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]

                if nums[i] == j:
                    dp[i][j] = True
                    continue
                if nums[i] < j:
                    # 如果当前数比要求的和小，那么看状态矩阵中的前一个状态是否满足，或者上一个状态的和是否可以凑成j减去当前数
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

        return dp[n - 1][target]

    def canPartition_2(self, nums):
        n = len(nums)
        if n == 0:
            return False
        sum = 0
        for num in nums:
            sum += num
        if sum % 2 != 0:
            return False
        target = sum // 2
        dp = [[False for _ in range(target + 1)] for _ in range(n)]
        if nums[0] == target:
            dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

            # 由于状态转移方程的特殊性，提前结束，可以认为是剪枝操作
            if dp[i][target]:
                return True
        return dp[n - 1][target]

    def canPartition_3(self, nums):
        n = len(nums)
        if n == 0:
            return False
        sum = 0
        for num in nums:
            sum += num
        if sum % 2 != 0:
            return False
        target = sum // 2
        dp = [False for _ in range(target + 1)]
        # 第一个数小于等于target时，状态矩阵对应的位置设置为true
        # https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-xiang-jie-zhen-dui-ben-ti-de-yo/406696/
        # 记录了当时的讨论
        if nums[0] <= target:
            dp[nums[0]] = True
        for i in range(1, n):
            for j in range(target, 0, -1):
                # 因为是从后往前进行运算，所以如果nums[i]>j那么，nums[i]肯定大于后边的j，这里就直接退出循环，相当于剪枝
                if nums[i] > j:
                    break
                if dp[target]:
                    return True
                dp[j] = dp[j] or dp[j - nums[i]]

        return dp[target]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 5, 11, 5]
    nums = [1, 2, 5]
    nums = [15, 5, 5, 5]
    print(solution.canPartition_3(nums))
