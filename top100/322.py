# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/7 21:00
'''
solution1: 暴力的动态规划
solution2: 带有备忘录的动态规划，在备忘录中存储每一个计算过的总钱数需要的硬币数，那么在遍历的过程中就会省去重复计算。
solution3: 动态转移矩阵的动态规划。
solution4: dfs。将硬币从大到小排序，从最大的硬币开始，先用尽量大的硬币数量，使总金额减去硬币金额尽量小，然后在使用小金额进行相同的操作，
同时记录在凑满总金额时用的最少的硬币个数。
'''
import math
class Solution:
    # 暴力解法，超时
    def coinChange_1(self, coins, amount):

        def dp(n):
            if n == 0: return 0
            if n < 0: return -1
            res = float('inf')
            for coin in coins:
                sub = dp(n - coin)
                if sub == -1: continue
                res = min(res, 1 + sub)
            return res if res != float('inf') else -1

        return dp(amount)

    def coinChange_2(self, coins, amount):
        memo = {}

        def dp(n):
            if n in memo: return memo[n]
            if n == 0: return 0
            if n < 0: return -1
            res = float('inf')
            for coin in coins:
                sub = dp(n - coin)
                if sub == -1: continue
                res = min(res, sub + 1)
            memo[n] = res if res != float('inf') else -1
            return memo[n]

        return dp(amount)

    def coinChange_3(self, coins, amount):
        # 因为对于amount，最大的硬币数就是amount个了，所以这里设置初始值为amount+1，相当于一个没有意义的数。
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == amount + 1 else dp[amount]

    def coinChange_4(self, coins, amount):
        n = len(coins)
        # 使硬币金额倒叙，从最大的开始
        coins = sorted(coins, reverse=True)
        res = amount + 1

        def dfs(index, target, count):
            nonlocal res
            this_coin = coins[index]
            # 如果当前的硬币来凑剩余的target的数量加上之前累积的硬币数count大于等于之前的解res，那么舍去这种方法
            # math.ceil()是向上取整，例如10/3=4
            if count + math.ceil(target / this_coin) >= res:
                return
            # 如果剩余的target能够整除当前的硬币金额，那么记录下当前解
            if target % this_coin == 0:
                res = count + target // this_coin
            # 如果当前的index已经是最后一个了，那么后边就不需要再去计算了，说明所有的硬币都凑过了，但是没凑全
            if index == n - 1:
                return
            # 这里就是一个dfs搜索，先用最大的硬币来凑，然后逐次递减硬币的金额，如果当前硬币金额大于target，那么target//this_coin=0，也就是使用0个当前硬币
            for i in range(target // this_coin, -1, -1):
                dfs(index + 1, target - i * this_coin, count + i)

        dfs(0, amount, 0)
        return -1 if res == amount + 1 else res



if __name__ == '__main__':
    solution = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(solution.coinChange_4(coins, amount))
