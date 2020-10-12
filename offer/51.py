# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/10 16:32
'''
solution: 利用归并排序的分治思想，先拆分，在合并的时候计算逆序对。
https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/
'''
class Solution:
    def reversePairs(self, nums):
        size = len(nums)
        if size < 2:
            return 0
        temp = [0 for _ in range(size)]

        return self.count_reverse_pairs(nums, 0, size - 1, temp)

    def count_reverse_pairs(self, nums, left, right, temp):
        if left == right:
            return 0
        mid = (left + right) >> 1
        left_pairs = self.count_reverse_pairs(nums, left, mid, temp)
        right_paris = self.count_reverse_pairs(nums, mid + 1, right, temp)

        # 这里已经是排好序的两个子序列，如果左序列最后一个小于右序列第一个，说明两个序列之间没有逆序对。
        # 直接返回左序列内的逆序对和右序列内的逆序对。
        if nums[mid] <= nums[mid + 1]:
            return left_pairs + right_paris

        # 合并两个序列，并计算两个序列之间的逆序对。
        reverse_cross_pairs = self.merge_reverse_pairs(nums, left, mid, right, temp)
        return left_pairs + right_paris + reverse_cross_pairs

    def merge_reverse_pairs(self, nums, left, mid, right, temp):
        for i in range(left, right + 1):
            temp[i] = nums[i]

        i = left
        j = mid + 1
        res = 0

        for k in range(left, right + 1):
            if i > mid:
                nums[k] = temp[j]
                j += 1
            elif j > right:
                nums[k] = temp[i]
                i += 1
            # 左序列比右序列小，直接将小的赋值给nums，不计算逆序对
            elif temp[i] <= temp[j]:
                nums[k] = temp[i]
                i += 1
            # 右序列比左序列小，需要将小的赋值给nums，并计算逆序对，逆序对的计算方法为，左序列有多少个元素：mid-i+1。
            elif temp[i] >= temp[j]:
                nums[k] = temp[j]
                j += 1
                res += (mid - i + 1)
        return res



solution = Solution()
nums = [7, 5, 6, 4, 1]
print(solution.reversePairs(nums))
