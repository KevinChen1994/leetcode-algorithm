# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/24 17:55

class Solution:
    def printNumbers(self, n: int):
        res = list(range(1, 10 ** n))
        return res


if __name__ == '__main__':
    solution = Solution()
    n = 1
    print(solution.printNumbers(n))
