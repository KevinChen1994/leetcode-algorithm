# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/14 21:47
'''
https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/zhi-chu-xian-yi-ci-de-shu-xi-lie-wei-yun-suan-by-a/
'''
class Solution:
    def singleNumbers(self, nums):
        ret = 0
        a = 0
        b = 0
        for num in nums:
            ret = ret ^ num
        h = 1
        while h & ret == 0:
            h <<= 1
        for num in nums:
            if h & num == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]


solution = Solution()
nums = [1, 2, 10, 4, 1, 4, 3, 3]
print(solution.singleNumbers(nums))
