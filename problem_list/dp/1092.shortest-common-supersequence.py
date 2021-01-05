# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/5 15:10
'''
solution: 利用最长公共子序列，使用逆向思维来倒推最短公共超序列：从后往前在最长公共子序列中插入不属于最长公共子序列的值。
思路是这样的，先使用dp求出最长公共子序列的长度，并在dp中存储每个阶段的最长公共子序列，dp[i][j]代表str1[0:i]与str2[0:j]的最长公共子序列。
然后分情况讨论：
1. str1或str2有一个是空，那将非空作为最短公共超序列。
2. str1[l1] == str2[l2]，也就是两个序列的最后一个字符相等，那么插入任意一个，并且两个序列同时减一；
3. str1[l1] != str2[l2]
3.1. dp[l1-1][l2] == dp[l1][l2]，也就是说l1的最后一个字符不属于最长公共子序列，那将str1[l1]插入最短公共超序列，l1减一；
3.2. dp[l1][l2-1] == dp[l1][l2]，也就是说l2的最后一个字符不属于最长公共子序列，那将str2[l2]插入最短公共超序列，l2减一；
'''
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        ans = ''
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        while l1 or l2:
            if not l1:
                c = str2[l2 - 1]
                l2 -= 1
            elif not l2:
                c = str1[l1 - 1]
                l1 -= 1
            elif dp[l1 - 1][l2] == dp[l1][l2]:
                c = str1[l1 - 1]
                l1 -= 1
            elif dp[l1][l2 - 1] == dp[l1][l2]:
                c = str2[l2 - 1]
                l2 -= 1
            else:
                c = str1[l1 - 1]
                l1 -= 1
                l2 -= 1
            ans = c + ans
        return ans


if __name__ == '__main__':
    solution = Solution()
    str1 = "abac"
    str2 = "cacbc"
    # "cacbac"
    print(solution.shortestCommonSupersequence(str1, str2))
