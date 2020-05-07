# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/7 21:00
'''
solution1: 暴力的动态规划
solution2: 带有备忘录的动态规划，在备忘录中存储每一个计算过的总钱数需要的硬币数，那么在遍历的过程中就会省去重复计算。
solution3: 动态转移矩阵的动态规划。
solution4: dfs
'''
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


if __name__ == '__main__':
    solution = Solution()
    coins = [1, 2, 5]
    amount = 10
    print(solution.coinChange_3(coins, amount))
