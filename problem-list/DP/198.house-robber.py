# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/23 15:55
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = max((dp[i - 2] if i > 1 else 0) + nums[i], dp[i - 1] if i > 0 else 0)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 9, 3, 1]
    print(solution.rob(nums))
