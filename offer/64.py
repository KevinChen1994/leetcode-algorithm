# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/23 15:08
'''
solution1:
solution2: 递归。终止条件是n=1，所以利用短路来实现，当n=1时，n > 1 and self.sumNums_1(n - 1)短路，终止递归。
'''
class Solution:
    def sumNums(self, n: int) -> int:
        return sum(range(n + 1))

    def __init__(self):
        self.res = 0

    def sumNums_1(self, n: int) -> int:
        n > 1 and self.sumNums_1(n - 1)
        self.res += n
        return self.res


solution = Solution()
n = 9
print(solution.sumNums_1(n))
