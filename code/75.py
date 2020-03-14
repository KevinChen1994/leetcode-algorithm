# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/14 21:51
# software: PyCharm
'''
solution1: 快排
solution2: 三指针；首尾各一个指针，分别代表指向0和2的位置，另外一个指向开头的指针，如果当前指针所指的值为0，那么就与0所指位置交换，并同时向前移动这两个指针；
如果当前指针所指的值为2，那么就与2所指的指针交换，并向后移动2所指指针，当前指针不动；如果当前指针所指的值为1，那么向前移动1所指指针。
'''

class Solution:
    def sortColors_1(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums, 0, len(nums) - 1)
        print(nums)

    def quick_sort(self, li, start, end):
        # 分治 一分为二
        # start=end ,证明要处理的数据只有一个
        # start>end ,证明右边没有数据
        if start >= end:
            return
        # 定义两个游标，分别指向0和末尾位置
        left = start
        right = end
        # 把0位置的数据，认为是中间值
        mid = li[left]
        while left < right:
            # 让右边游标往左移动，目的是找到小于mid的值，放到left游标位置
            while left < right and li[right] >= mid:
                right -= 1
            li[left] = li[right]
            # 让左边游标往右移动，目的是找到大于mid的值，放到right游标位置
            while left < right and li[left] < mid:
                left += 1
            li[right] = li[left]
        # while结束后，把mid放到中间位置，left=right
        li[left] = mid
        # 递归处理左边的数据
        self.quick_sort(li, start, left - 1)
        # 递归处理右边的数据
        self.quick_sort(li, left + 1, end)

    def sortColors_2(self, nums):
        left = 0
        right = len(nums) - 1
        cur = 0
        while cur <= right:
            if nums[cur] == 0:
                self.swap(nums, cur, left)
                cur += 1
                left += 1
            elif nums[cur] == 2:
                self.swap(nums, cur, right)
                right -= 1
            else:
                cur += 1
        print(nums)

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    print(solution.sortColors_2(nums))
