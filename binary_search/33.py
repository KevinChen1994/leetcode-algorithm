# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/21 15:11

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # mid之前是从小到大排序的
            if nums[left] <= nums[mid]:
                if nums[mid] > target and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            # mid之后是从小到大排序的
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 2
    nums = [3, 1]
    target = 1
    print(solution.search(nums, target))
