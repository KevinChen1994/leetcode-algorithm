# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/26 21:36
'''
solution1: 两次遍历寻找左边界和右边界。
solution2: 一次遍历。
'''

class Solution:
    def findUnsortedSubarray_1(self, nums):
        n = len(nums)
        max = nums[0]
        min = nums[n - 1]
        left = 0
        right = -1
        for i in range(n):
            if max > nums[i]:
                right = i
            else:
                max = nums[i]
        for i in range(n - 1, -1, -1):
            if min < nums[i]:
                left = i
            else:
                min = nums[i]
        return right - left + 1

    def findUnsortedSubarray_2(self, nums):
        n = len(nums)
        max = nums[0]
        min = nums[n - 1]
        left = 0
        right = -1
        for i in range(n):
            if max > nums[i]:
                right = i
            else:
                max = nums[i]
            if min < nums[n - i - 1]:
                left = n - i - 1
            else:
                min = nums[n - i - 1]
        return right - left + 1


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(solution.findUnsortedSubarray_2(nums))
