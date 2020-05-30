# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/31 23:01
# software: PyCharm
'''
solution1: 遍历一遍，每次记录当前价格与最低价格的差值和最低的价格。
solution2: 使用单调栈。在prices最后添加0，作用是最后能把栈弹空。在遍历过程中，如果栈为空或者当前价格高于栈底价格则进栈；
如果当前价格低于栈底价格，那么循环弹出栈，并在弹出过程中计算弹出价格与栈底元素的差(即收益)，记录最大收益。
'''
class Solution:
    def maxProfit_1(self, prices):
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit

    def maxProfit_2(self, prices):
        ans = 0
        prices.append(0)
        stack = []
        for i in prices:
            if len(stack) == 0:
                stack.append(i)
            elif stack[0] < i:
                stack.append(i)
            else:
                while len(stack) != 0 and stack[-1] > i:
                    ans = max(ans, stack[-1] - stack[0])
                    stack.pop()
                stack.append(i)
        return ans




if __name__ == '__main__':
    solution = Solution()
    # prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 6, 4, 3, 1]
    # prices = [2, 1, 4]
    # prices = [2, 5, 1, 3]
    prices = []
    print(solution.maxProfit_2(prices))
