# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/11/26 23:50
'''
solution: 转换成0-1背包问题，自下而上使用动态规划，dp[i][j]代表i个0和j个1能装的最多个字符串个数。
动态转移矩阵就是dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)
其中zero代表当前字符串包含的0的个数，one代表当前字符串包含的1的个数。
'''
class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for str in strs:
            one = str.count('1')
            zero = str.count('0')
            # zero, one = self.calZeroAndOne(str)
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)
        return dp[m][n]

    def calZeroAndOne(self, s):
        zero = 0
        one = 0
        for c in s:
            if c == '0':
                zero += 1
            if c == '1':
                one += 1
        return zero, one


if __name__ == '__main__':
    solution = Solution()
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print(solution.findMaxForm(strs, m, n))
