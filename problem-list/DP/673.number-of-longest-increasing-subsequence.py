# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/3/5 16:05
from typing import List
'''
solution: 这道题是对leetcode-300的进阶版本，在300中只需要记录最长的序列长度就可以了，但是这道题需要记录下序列长度的个数，
所以定义两个dp序列，一个记录递增序列最大长度lengths，一个记录递增序列个数counts。
如何更新lengths，其实跟300的思路是一样的，遇到比当前的数字小的数字去判断，以哪个数字结尾的长度大就好了。
如何更新counts比较麻烦，需要判断以当前数字为结尾和以比当前数字小的那个数字为结尾的递增序列的长度，
如果小的那个数字的长度大于等于当前的数字的长度，那么说明如果以当前数字为结尾的话，长度会更长，那么更新当前的长度个数为小的那个数字的长度个数；
如果小的那个数字的长度个数加一跟当前数字长度的个数，那么说明加上当前数字的长度两个长度是一样的，那么更新当前数字长度为两个数量之和。
如果文字描述的不清楚，debug看一下数字其实就明白了。
最后需要遍历所有的长度个数，如果长度等于最长的那个长度，将长度个数累加就是结果。
'''

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # 以nums[i]为结尾的最长的递增序列长度
        lengths = [1 for _ in range(n)]
        # 以nums[i]结尾的的最长的递增序列的个数
        counts = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # 说明找到了一个比以nums[i]结尾的递增序列更长的递增序列，这时需要counts[i]的个数就等于counts[j]的个数
                    if lengths[j] >= lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    # 说明以nums[i]结尾的递增序列与以nums[j]结尾的递增序列的个数相等，那么需要将两个序列的个数相加
                    elif lengths[i] == lengths[j] + 1:
                        counts[i] += counts[j]
        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 5, 4, 7]
    print(solution.findNumberOfLIS(nums))
