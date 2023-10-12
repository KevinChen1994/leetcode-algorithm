# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/3/3 16:45
'''
solution: 最开始的思路是先将当前的数开平方，然后用当前的数减去最大的平方和，这样就可以通过dp去获取平方和的次数再加1就好了。
也就是dp[i] = dp[i-j**2] + 1，j是最大的平方和，j<i。但是这样就可能忽略一点，没有取最少的次数。例如：dp[12] =dp[3] + 1 = 4.
这样不是最少的，所以需要进行优化。
首先需要在最小的平方和之内一个一个去遍历，找到一直去计算dp[i] = min(dp[i], dp[j] + 1)。但是这样会超时。
所以需要提前计算好所有的平方和，存储起来，以减少运算。
'''

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        for i in range(1, n + 1):
            for j in squares:
                if j > i:
                    break
                dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    n = 12
    print(solution.numSquares(n))
