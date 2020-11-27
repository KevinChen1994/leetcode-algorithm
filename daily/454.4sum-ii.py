# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/11/27 21:54
'''
solution: 将四个数组，两两合并，然后计算每个之间的和，进行判断即可。
'''
from typing import List
import collections


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ab_dict = collections.defaultdict(int)
        # ab_dict = {}
        res = 0
        for i in A:
            for j in B:
                ab_dict[i + j] += 1
        for i in C:
            for j in D:
                res += ab_dict[-i - j]
        return res


if __name__ == '__main__':
    solution = Solution()
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(solution.fourSumCount(A, B, C, D))
