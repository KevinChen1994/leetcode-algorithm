# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/30 17:28
'''
solution1: 两次遍历，使用双指针法。第一遍遍历，现将是0的位置的数用下一个不是0的数替换（这是会出现重复的数，后边这个数也会被下一个非零的数替换）。
j这个指针相当于记录了有多少个非零的数。第二编遍历就是从j开始，将后边的数全置为零。
solution2: 一次遍历，借用快排思想。在遍历过程中，遇到不是0的数就将该数放到0的左边，是0的就在0的右边。
solution3: 对solution2的优化，在solution2中，即使i与j指向的是同一个且非零元素也会进行交换，这样会浪费时间，这里可以进行优化。只有j指向的是0，i指向的是非零，
并且i比j的情况下才进行交换。
'''
class Solution:
    def moveZeroes_1(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0

    def moveZeroes_2(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

    def moveZeroes_3(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i > j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1



if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    # nums = [1,2,3,4]
    solution.moveZeroes_3(nums)
