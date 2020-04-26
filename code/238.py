# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/26 21:59
'''
solution: 乘积=当前数左边的乘积*当前数右边的乘积。第一次遍历，outputs中存储的是当前数左边的乘积，第二次遍历用outputs中的数乘上right，right是一个累乘，
存储的是当前数右边的乘积。
'''
class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        outputs = [0] * length
        outputs[0] = 1
        for i in range(1, length):
            outputs[i] = outputs[i - 1] * nums[i - 1]
        right = 1
        for i in reversed(range(length)):
            outputs[i] = outputs[i] * right
            right *= nums[i]
        return outputs


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4]
    print(solution.productExceptSelf(nums))
