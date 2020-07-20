# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/20 23:31

class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 4, 5, 1, 2]
    print(solution.findMin(nums))
