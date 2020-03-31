# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/31 23:01
# software: PyCharm

class Solution:
    def maxProfit(self, prices):
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


if __name__ == '__main__':
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 6, 4, 3, 1]
    # prices = [2, 1, 4]
    print(solution.maxProfit(prices))
