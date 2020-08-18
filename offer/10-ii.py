# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/12 22:06

class Solution:
    def numWays(self, n: int) -> int:
        dp = [1, 1, 2]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n] % 1000000007

if __name__ == '__main__':
    solution = Solution()
    n = 10
    print(solution.numWays(7))
