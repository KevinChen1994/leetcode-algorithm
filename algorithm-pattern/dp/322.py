# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/2 14:50
'''
solution: 动态规划的思想就是，想要解决fn(5)，那么就要先解决fn(4)，依次类推，那么这里dp数组就定义amount为n时的解为多少。
动态转移矩阵就是，min(dp[i], dp[i - coin] + 1)
'''
class Solution:
    def coinChange(self, coins, amount) -> int:
        # 初始化dp数组为amount+1，硬币个数最多为amount个，所以大于amount就是一个无意义的数。
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[-1] == amount + 1 else dp[-1]


if __name__ == '__main__':
    solution = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(solution.coinChange(coins, amount))
