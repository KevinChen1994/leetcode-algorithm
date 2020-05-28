# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/26 21:36
'''
solution1: 两次遍历寻找左边界和右边界。如果max大于nums[i]，就将右边界更新为i，然后更新max。如果min小于nums[j]，就将左边界更新为j，然后更新min
solution2: 一次遍历。
solution3: 先将nums排序为sorted_nums，然后从左到右判断，nums与sorted_nums从哪个开始不一样，记为左边界；从右到左判断，nums与sorted_nums从哪个开始不一样，记为右边界。
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

    def findUnsortedSubarray_3(self, nums):
        nums_sorted = sorted(nums)
        n = len(nums)
        i = 0
        j = n-1
        while i < n and nums_sorted[i] == nums[i]:
            i += 1
        while j > i and nums_sorted[j] == nums[j]:
            j -= 1
        return j - i + 1



if __name__ == '__main__':
    solution = Solution()
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(solution.findUnsortedSubarray_3(nums))
