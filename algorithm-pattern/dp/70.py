# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/23 14:06

class Solution:
    def climbStairs(self, n: int) -> int:
        # n+1是为了防止出现只有一阶台阶的情况
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]


if __name__ == '__main__':
    solution = Solution()
    n = 1
    print(solution.climbStairs(n))
