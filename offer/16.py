# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/20 21:52
import math

math.pow()


class Solution:
    # 超时
    def myPow_1(self, x: float, n: int) -> float:
        res = 1
        if n > 0:
            for i in range(n):
                res *= x
        elif n < 0:
            for i in range(n, 0):
                res *= x
            res = 1 / res
        else:
            res = 1
        return res

    # 位运算
    def myPow_2(self, x, n):
        res = 1
        if x == 0:
            return 0
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    x = 2.0000
    n = 10
    print(solution.myPow_2(x, n))
