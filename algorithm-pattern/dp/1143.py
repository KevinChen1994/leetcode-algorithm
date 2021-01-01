# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/30 20:10
'''
solution: 定义一个dp数组，每个位置所代表的元素，dp[i][j]为text1[0:i]与text2[0:j]之间最大的公共子序列。那么状态转移就很好解决了，如果当前元素相同，那么就是在上一个状态上加1就好，
如果不想相同，只需要判断dp[i-1][j]与dp[i][j-1]哪个大就好了。这个过程可以参考递归的代码来理解。
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    def longestCommonSubsequence_recursion(self, text1, text2):
        def dp(i, j):
            if i == -1 or j == -1:
                return 0
            if text1[i] == text2[j]:
                return dp(i - 1, j - 1) + 1
            else:
                return max(dp(i - 1, j), dp(i, j - 1))

        return dp(len(text1) - 1, len(text2) - 1)


if __name__ == '__main__':
    solution = Solution()
    text1 = 'abcde'
    text2 = 'ace'
    print(solution.longestCommonSubsequence(text1, text2))
