# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/14 23:33
'''
solution: 滑动窗口
'''
class Solution:
    def findContinuousSequence(self, target: int):
        res = []
        tmp = []
        left = 1
        right = 1
        while left <= target // 2:
            if sum(tmp) < target:
                tmp.append(right)
                right += 1
            elif sum(tmp) > target:
                tmp.pop(0)
                left += 1
            else:
                res.append(tmp[:])
                tmp.pop(0)
                left += 1
        return res



solution = Solution()
target = 9
print(solution.findContinuousSequence(target))
