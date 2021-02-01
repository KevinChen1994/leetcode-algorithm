# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/1 10:42
from typing import List
'''
solution: 利用快排的思想，第k大的元素，索引就是len-k,通过“分”每次确定一个pivot，如果pivot与最大元素的索引相同，直接返回，
否则继续进行寻找。
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick(nums, 0, len(nums) - 1, len(nums) - k)

    def quick(self, nums, left, right, k):
        pivot = self.partition(nums, left, right)
        if pivot == k:
            return nums[k]
        elif pivot > k:
            return self.quick(nums, left, pivot - 1, k)
        else:
            return self.quick(nums, pivot + 1, right, k)

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
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(solution.findKthLargest(nums, k))
