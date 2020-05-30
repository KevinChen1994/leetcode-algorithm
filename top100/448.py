# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/21 18:32
'''
solution1: 原地修改数组。先遍历一遍数组，在每一个数组元素做一个处理，将当前元素的绝对值-1，得到的数作为新的索引，然后将该索引下的数变成负数，
再次遍历数组的时候，从1开始遍历，当i-1索引下的数大于零时，说明这个位置的数在之前没有遍历到，那么就是缺少这个数。这个方法不好想，太tricky了。
solution2: 利用set去重
'''

class Solution:
    def findDisappearedNumbers_1(self, nums):
        ans = []
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                ans.append(i)
        return ans

    def findDisappearedNumbers_2(self, nums):
        ans = []
        n = len(nums)
        nums = set(nums)
        for i in range(1, n+1):
            if i not in nums:
                ans.append(i)
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(solution.findDisappearedNumbers_2(nums))
