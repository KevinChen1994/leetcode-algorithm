# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/24 17:51
'''
solution1: 超时
solution2: 贪心算法
solution3: 动态规划，可以将dp数据放到nums数组中进行。
'''
class Solution:
    def maxSubArray_1(self, nums) -> int:
        res = float('-inf')
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum > res:
                    res = sum
        return res

    def maxSubArray_2(self, nums):
        res = nums[0]
        tmp = 0
        for i in range(len(nums)):
            if tmp > 0:
                tmp += nums[i]
            else:
                tmp = nums[i]
            res = max(res, tmp)
        return res

    def maxSubArray_3(self, nums):
        # 如果上一个元素是正数，就加到当前元素上，如果不是，那给当前元素带来的只有负面影响，那就不加，保持原状。
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)

if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray_2(nums))
