# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/12/30 23:17
'''
solution: 依次列出前几个台阶每个台阶最大的次数，可以总结出规律，类似于斐波那契数列，dp[i] = dp[i-1] + dp[i-2]。
其物理意义也可以解释，因为每次只能选择挑一级或者两级，所以能到当前台阶有两种方式，一个是从上一个台阶跳一级，另外一个是从上两个台阶跳两级，
那当前台阶的最大次数也就是上一级的最大次数加上上两级的最大次数。
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    n = 4
    print(solution.climbStairs(n))