# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/18 22:39
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return
        res = 0
        tmp = float('inf')
        nums.sort()
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                if abs(nums[i] + nums[l] + nums[r] - target) < tmp:
                    tmp = abs(nums[i] + nums[l] + nums[r] - target)
                    res = nums[i] + nums[l] + nums[r]
                if nums[i] + nums[l] + nums[r] > target:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    return target
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [-4, -1, 2, 1, 1]
    target = 1
    nums = [0, 1, 2]
    target = 0
    print(solution.threeSumClosest(nums, target))
