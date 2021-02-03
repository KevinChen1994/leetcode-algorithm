# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/12/31 15:50

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        result = [0 for _ in range(n + 1)]
        result[0] = 0
        result[1] = 1
        result[2] = 1
        for i in range(3, n + 1):
            result[i] = result[i-1] + result[i-2] + result[i-3]
        return result[-1]

if __name__ == '__main__':
    solution = Solution()
    n = 25
    print(solution.tribonacci(n))