# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/14 22:47
'''
solution: 因为是递增排序数组，所以可以利用双指针，一个指向开头，一个指向结尾，两个指针所指数字相加，如果大于target，那么右指针左移，
如果小于target，那么左指针右移。
'''
class Solution:
    def twoSum(self, nums, target: int):
        left, right = 0, len(nums) - 1
        while left != right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                break
        return [nums[left], nums[right]]


solution = Solution()
nums = [10, 26, 30, 31, 47, 60]
target = 40
print(solution.twoSum(nums, target))
