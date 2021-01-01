# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/21 14:50

class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            # 如果中间值小于最右边的值，将范围锁定在[mid+1, right]中，如果right+1的话，重新计算mid时可能会错过最小值
            elif nums[mid] < nums[right]:
                right = mid
            # 一点点缩小范围
            else:
                right -= 1
        return nums[left]


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 2, 2, 0, 1, 2]
    nums = [3, 1, 3]
    print(solution.findMin(nums))
