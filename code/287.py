# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/1 21:21
'''
solution1: 二分查找法。题目描述为当前有n+1个整数，数的范围是1到n，那么就可以通过判断当前序列中数的分布来确定重复的数字是哪个。
（此原理称为抽屉原理，即桌上有十个苹果，要把这十个苹果放到九个抽屉里，无论怎样放，我们会发现至少会有一个抽屉里面放不少于两个苹果。）
先确定1到n之间的中位数，然后判断序列中的数是否比中位数小，如果小就进行计数，一次遍历之后，如果比中位数小的数的个数比中位数还多，
说明重复数字在中位数左边，否则在右边。

'''
class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        left = 1
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 4, 2, 2]
    print(solution.findDuplicate(nums))
