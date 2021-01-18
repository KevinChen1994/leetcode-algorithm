# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/8 16:53
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in num_dict:
                return i, num_dict[target - nums[i]]
            else:
                num_dict[nums[i]] = i


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 5, 11, 15, 5]
    target = 10
    print(solution.twoSum(nums, target))
