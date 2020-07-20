# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/20 18:08

class Solution:
    def search(self, nums, target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1


solution = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(solution.search(nums, target))
