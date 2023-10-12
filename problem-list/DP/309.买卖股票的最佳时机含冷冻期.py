# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/23 16:37
from typing import List
'''
solution: 对top100-309的空间优化
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = 0
        rest = 0
        hold = float('-inf')
        for price in prices:
            # 上一个时刻卖出获得的全部收益
            prev_sold = sold
            sold = hold + price
            # rest - price说明了已经在冷静期了，所以可以购买
            hold = max(hold, rest - price)
            rest = max(rest, prev_sold)
        return max(rest, sold)


if __name__ == '__main__':
    solution = Solution()
    prices = [1, 2, 3, 0, 2]
    print(solution.maxProfit(prices))
