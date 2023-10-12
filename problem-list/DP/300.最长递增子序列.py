# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/3/5 15:15
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(solution.lengthOfLIS(nums))
