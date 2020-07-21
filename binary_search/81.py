# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/21 16:29

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # 如果遇到重复的情况，那么就一直遍历到不重复为止，此时就跟33题一样了
            if nums[left] == nums[mid]:
                left += 1
                continue
            if nums[left] <= nums[mid]:
                if nums[mid] > target and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 1
    print(solution.search(nums, target))
