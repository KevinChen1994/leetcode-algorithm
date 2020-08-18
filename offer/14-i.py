# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/18 22:10
'''
solution: 假设每次均分绳子能取得最大的乘积和，经过数学运算，可得将绳子尽可能多的切分为长度为3的片段，不足为3的，
如果是1，那么从前一个3中，拿出一个，凑出两个2，如果是2，则不补。
参考https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/
'''
import math

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)


if __name__ == '__main__':
    solution = Solution()
    n = 10
    print(solution.cuttingRope(n))
