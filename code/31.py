# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/2/27 18:05
# software: PyCharm


'''
题干的意思是：找出这个数组排序出的所有数中，刚好比当前数大的那个数
比如当前 nums = [1,2,3]。这个数是123，找出1，2，3这3个数字排序可能的所有数，排序后，比123大的那个数 也就是132
如果当前 nums = [3,2,1]。这就是1，2，3所有排序中最大的那个数，那么就返回1，2，3排序后所有数中最小的那个，也就是1，2，3 -> [1,2,3]

解题思路：例如给定数组为[1,2,3,4,5,6]，那么它的组合有123456，123465，123546......654321。
1. 当希望找到一个更大的数时，只需要将后边大的数与前边小的数交换即可；例如123456 < 123465
2. 并且还需要控制增加的幅度尽可能小，那么就需要尽可能从右边去进行交换；将一个尽可能小的大数与前边的小数进行交换，
例如123465，下一个排列是将5与4进行交换，而不是6与4；大数交换到前边后，将大数后边的全部数字置为升序，升序就是最小排列，
例如上一步将5与4交换后得到123564，将5右边的数置为升序，即123546。

'''


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                k = i - 1
                flag = 1
                break
        if flag == 1:
            for i in range(len(nums) - 1, k, -1):
                if nums[i] > nums[k]:
                    tmp = nums[k]
                    nums[k] = nums[i]
                    nums[i] = tmp
                    self.quick_sort(nums, k + 1, len(nums) - 1)
                    break
        else:
            self.quick_sort(nums,0, len(nums) - 1)

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


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2]
    solution.nextPermutation(nums)
    print(nums)
