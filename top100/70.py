# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/12 10:49
# software: PyCharm

'''
solution1: 使用递归。思想是回溯法，如果当前值cur等于n那么就返回1，最终结果就是每次登一个台阶和两个台阶的和。
感觉自己说不清楚。
solution2: 动态规划。通过手算可以得出，n个台阶的不同路径等于n-1和n-2两个路径之和，那么直接使用dp数组存储就好。
solution3: 通过观察发现，这个登台阶的路径数就是一个斐波那契数列。0 1 1 2 3 5 8...
'''


class Solution:
    # 超时
    def climbStairs_1(self, n):
        return self.backtrack(n, 0)

    def backtrack(self, n, cur):
        if cur > n:
            return 0
        if cur == n:
            return 1
        return self.backtrack(n, cur + 1) + self.backtrack(n, cur + 2)

    # 动态规划
    def climbStairs_2(self, n):
        # n+1 是为了防止出现只有1阶台阶的情况
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n-1]

    #斐波那契数列
    def climbStairs_3(self, n):
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second



if __name__ == '__main__':
    solution = Solution()
    n = 5
    print(solution.climbStairs_3(n))
