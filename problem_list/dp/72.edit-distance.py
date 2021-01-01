# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/12/30 22:58

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j],
                                   dp[i][j - 1],
                                   dp[i - 1][j - 1]) + 1
        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    word1 = "horse"
    word2 = "ros"
    print(solution.minDistance(word1, word2))