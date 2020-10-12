# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/12 15:29
'''
solution: 分别找到序列左边第一个等于target的索引和右边最后一个等于target的索引，两个索引相减加1即为结果
'''
class Solution:
    def search(self, nums, target: int) -> int:
        i = 0
        j = len(nums) - 1
        # 找到左边界第一个等于target的索引
        while i <= j:
            mid = (i + j) >> 1
            if nums[mid] >= target:
                j = mid - 1
            else:
                i = mid + 1
        left = i
        # 如果左边没有提前终止程序
        if i <= len(nums) - 1 and nums[i] != target:
            return 0
        # 找到右边界最后一个等于target的索引
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) >> 1
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        right = j
        return right - left + 1


solution = Solution()
nums = [5, 7, 8, 8, 8, 9]
target = 8
print(solution.search(nums, target))
