# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/7 17:59
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        tmp = 0
        for i in range(len(nums)):
            if tmp > 0:
                tmp += nums[i]
            else:
                tmp = nums[i]
            ans = max(ans, tmp)
        return ans



if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums))
