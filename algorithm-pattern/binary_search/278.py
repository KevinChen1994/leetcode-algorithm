# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/20 23:20
'''
solution: 当检测到错误时，让右边界等于mid就好，不需要做别的处理，left会一点点逼近最前错误的那个点。
'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            elif not isBadVersion(mid):
                left = mid + 1
        return left
