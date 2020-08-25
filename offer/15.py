# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/20 21:29
'''
solution: 与运算，两个都是1结果才是1，否则为0.
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

if __name__ == '__main__':
    solution = Solution()
    n = '00000000000000000000000000001011'
    print(solution.hammingWeight(n))