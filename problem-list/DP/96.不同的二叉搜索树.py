# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/3/12 10:43
'''
solution: top100-96讲的很清楚
'''

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    n = 3
    print(solution.numTrees(n))
