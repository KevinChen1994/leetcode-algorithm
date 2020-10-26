# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/22 16:40

class Solution:
    def maxProfit(self, prices) -> int:
        min_ = float('inf')
        res = 0
        for i in range(len(prices)):
            min_ = min(min_, prices[i])
            res = max(res, prices[i] - min_)
        return res


solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(solution.maxProfit(prices))
