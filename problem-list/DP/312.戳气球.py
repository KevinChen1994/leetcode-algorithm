from typing import List
'''
这道题的难点在于如何通过当前获取的金币数来推断下一次操作的金币数，所以我们采取从后往前算的思路，
也就是先计算最后一个被戳破的气球获取的金币数，来推断戳破前边气球能获取的金币数，选择最大的就是答案。
最后一个戳破的气球的计算方法，就是当前气球乘上左右两边的气球，并加上当前气球左区间和右区间能获取的最大的金币数。
'''

class Solution:
    # 官方题解：https://leetcode.cn/problems/burst-balloons/solutions/336390/chuo-qi-qiu-by-leetcode-solution/
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        nums = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = nums[i] * nums[k] * nums[j]
                    total += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)
        return dp[0][n + 1]
    
    # https://leetcode.cn/problems/burst-balloons/solutions/337630/zhe-ge-cai-pu-zi-ji-zai-jia-ye-neng-zuo-guan-jian-/
    def maxCoins2(self, nums: List[int]) -> int:
        # nums前后都加上1
        nums = [1] + nums + [1]
        # 定义dp矩阵，dp[i][j]代表(i,j)开区间里获取的最大的硬币数
        dp = [[0] * len(nums) for _ in range(len(nums))]

        # 计算所有区间，区间长度从3开始，n为区间结束索引，从2开始
        for n in range(2, len(nums)):
            # 对于每一个区间，区间开始索引为0
            for i in range(0, len(nums) - n):
                # j为该区间结束索引
                j = i + n
                # k为该区间中最后一个被戳破的气球
                # 那当前区间的最大值就等于，戳破该气球获取的金币数，加上该气球左区间和右区间累计获取的金币数
                for k in range(i + 1, j):
                    total = nums[i] * nums[k] * nums[j]
                    total += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)
        return dp[0][len(nums) - 1]


if __name__ == '__main__':
    solution = Solution()
    nums = [3,1,5,8]
    res = solution.maxCoins(nums)
    res = solution.maxCoins2(nums)
    print(res)