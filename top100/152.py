# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/10 20:34
'''
solution1: 动态规划。记录当前最大和当前最小值，当前最大值为当前值乘当前最大值，当前最小值为当前值乘以当前最小值，如果当前值为负数，
那么交换当前最大值和当前最小值。
solution2: 如果nums中负数的个数为奇数个，那么中间的那个负数左右两边负数的个数一定为偶数，只需求两边最大值。如果nums中负数的个数为偶数个，
那么最大值就是nums相乘。如果遇到0，那么重置当前值为1。
'''
class Solution:
    def maxProduct_1(self, nums):
        if not nums: return
        ans = float('-inf')
        max_ = 1
        min_ = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                tmp = max_
                max_ = min_
                min_ = tmp
            max_ = max(nums[i], max_ * nums[i])
            min_ = min(nums[i], min_ * nums[i])
            ans = max(ans, max_)
        return ans

    def maxProduct_2(self, nums):
        rev_nums = nums[::-1]
        for i in range(1, len(nums)):
            # 如果nums[i-1]为0，将当前值重置为1
            nums[i] *= nums[i - 1] or 1
            rev_nums[i] *= rev_nums[i - 1] or 1
        return max(max(nums), max(rev_nums))


if __name__ == '__main__':
    solution = Solution()
    # nums = [2, 3, -2, 4]
    # nums = [-2, 3, -4]
    nums = [-4, -3, -2]
    # nums = [1, 2, 3, 4, -5, 6, 7]
    print(solution.maxProduct_2(nums))
