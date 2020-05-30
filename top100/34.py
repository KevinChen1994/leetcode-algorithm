# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/2/29 21:53
# software: PyCharm
'''
与33题类似，使用二分查找的方法来解决。不同的一点是返回值是一个范围
思路就是先通过二分查找找到与target相同的一个索引，然后以该索引为中心，向前向后分别探索，找到所有相同值的索引
'''


class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                i, j = mid, mid
                while i > 0 and nums[i - 1] == target:
                    i -= 1
                while j < len(nums) - 1 and nums[j + 1] == target:
                    j += 1
                return [i, j]
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(solution.searchRange(nums, target))
