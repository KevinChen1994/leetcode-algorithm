# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/12/30 16:07
from typing import List
'''
solution: 与编辑距离类似，记dp[i][j]为nums1[0:i]与nums2[1:j]最大的点积。
那么分为三种情况：
1. 扔掉nums1[i]，dp[i][j] = dp[i-1][j]
2. 扔掉nums2[j]，dp[i][j] = dp[i][j-1]
3.1 使用nums1[i]和nums2[j]，dp[i][j] = dp[i-1][j-1] + nums1[i]*nums2[j]
3.2 当dp[i-1][j-1]<0时，扔掉nums1[i]与nums2[j]之前的，从nums1[i]和nums2[j]开始，dp[i][j] = nums1[i]*nums2[j]
'''

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[float('-inf') for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = max(dp[i][j - 1],
                               dp[i - 1][j],
                               max(0, dp[i - 1][j - 1]) + nums1[i - 1] * nums2[j - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    # nums1 = [2, 1, -2, 5]
    # nums2 = [3, 0, -6]
    nums1 = [3, 2, 7]
    nums2 = [2, -6, 7]
    # 输出：18
    # 解释：从nums1中得到子序列[2, -2] ，从nums2中得到子序列[3, -6] 。
    # 它们的点积为(2 * 3 + (-2) * (-6)) = 18 。

    print(solution.maxDotProduct(nums1, nums2))
