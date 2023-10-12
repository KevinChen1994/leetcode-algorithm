# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/23 16:11
from typing import List
'''
solution: leetcode-198的拓展，首尾不能同时偷，那就将nums分割成两个数组，一个只包含头，一个只包含尾，判断哪个大就好了。
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(self.my_rob(nums[:-1]), self.my_rob(nums[1:]))

    def my_rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = max((dp[i - 2] if i > 1 else 0) + nums[i], dp[i - 1] if i > 0 else 0)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 1]
    print(solution.rob(nums))
