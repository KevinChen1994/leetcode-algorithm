# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/12 21:58

class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n] % 1000000007


if __name__ == '__main__':
    solution = Solution()
    n = 5
    print(solution.fib(n))
