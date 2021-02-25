# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/24 15:43
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return nums[0]
        return self.quick_search(nums, 0, n - 1, n // 2)

    def quick_search(self, nums, left, right, k):
        pivot = self.partition(nums, left, right)
        if pivot == k:
            return nums[pivot]
        elif pivot > k:
            return self.quick_search(nums, left, pivot - 1, k)
        else:
            return self.quick_search(nums, pivot + 1, right, k)

    def partition(self, nums, left, right):
        target = nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[j] < target:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    nums = [2, 2]
    print(solution.majorityElement(nums))
