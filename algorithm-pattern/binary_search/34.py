# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/20 18:21
'''
solution: 注意寻找边界的时候，如果遇到nums[mid] == target，不需要返回，需要收紧另外一边的边界。
'''
class Solution:
    def searchRange(self, nums, target: int):
        return [self.left_bound(nums, target), self.right_bound(nums, target)]

    def left_bound(self, nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # 收紧右边界以锁定左边界
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def right_bound(self, nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # 收紧左边界以锁定右边界
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if right >= len(nums) or nums[right] != target:
            return -1
        return right


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(solution.searchRange(nums, target))
