# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/4 10:49
'''
solution1: 暴力法，很慢
solution2: 最快的方法，有点投机取巧的意思，直接算0.5次方，相当于开平方
solution3: 二分查找法，有点技巧在里边，相对暴力法快点
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        for num in range(1, x + 1):
            if num ** 2 == x:
                return num
            elif num ** 2 > x:
                return num - 1
        return 0

    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)

    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        while l <= r:
            mid = l + (r - l) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                r = mid - 1
            else:
                l = mid + 1
        return r

if __name__ == '__main__':
    solution = Solution()
    x = 9
    print(solution.mySqrt(x))