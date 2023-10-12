# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/3/2 22:10
'''
solution: 将问题进行转化，先转换为只有多米诺，发现是斐波那契数列，然后加入托米诺，就是多了两种状态。
参考花花酱讲的，思路很清晰：https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-790-domino-and-tromino-tiling/
'''

class Solution:
    def numTilings(self, N: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0, 0] for _ in range(N + 1)]
        dp[0][0] = dp[1][0] = 1
        for i in range(2, N + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 2][0] + 2 * dp[i - 1][1]) % MOD
            dp[i][1] = (dp[i - 2][0] + dp[i - 1][1]) % MOD
        return dp[N][0]

if __name__ == '__main__':
    solution = Solution()
    N = 3
    print(solution.numTilings(N))