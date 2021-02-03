# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/5 14:37

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 这里不需要考虑dp[i-1][j-1]，因为dp[i-1][j-1]肯定比其他两种情况要小。
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    text1 = "abcde"
    text2 = "ace"
    text1 = "abc"
    text2 = "def"
    text1 = "abc"
    text2 = "abc"
    print(solution.longestCommonSubsequence(text1, text2))
