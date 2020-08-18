# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/18 23:01
import math


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 1:
            return 3 ** (a - 1) * 4 % 1000000007
        if b == 2:
            return 3 ** a * 2 % 1000000007
        return 3 ** a % 1000000007


if __name__ == '__main__':
    solution = Solution()
    n = 1000
    print(solution.cuttingRope(n))
