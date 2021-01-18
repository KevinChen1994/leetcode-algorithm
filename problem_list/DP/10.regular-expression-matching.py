# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/12/31 16:06

# 给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。
#
'''
solution: dp[i][j]代表s[0:i]能否被p[0:j]匹配，分情况讨论：
1. s[i] = p[j] -> dp[i][j] = dp[i-1][j-1]
2. p[j] == '.' -> dp[i][j] = dp[i-1][j-1]
3. p[j] == '*'
3.1. p[j-1] != '.' and p[j-1] != s[i] -> dp[i][j] = dp[i-1][j-2] a*代表空
3.2. p[j-1] == '.' or p[j-1] == s[i] ->
dp[i][j] = dp[i-1][j] a*代表多个a
or dp[i][j] = dp[i][j-1] a*代表a
or dp[i][j] = dp[i][j-2] a*代表空

'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1 = len(s)
        l2 = len(p)
        dp = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        dp[0][0] = True
        # 这个循环是为了s = "aab" p = "c*aab"这种情况，因为c*可以代表空，所以这两个是匹配的。
        # 但是由于使用动态规划，初始化时只有dp[0][0]=True，那么在后续的遍历中并不能应用这个值。
        for j in range(2, l2 + 1):
            if p[j - 1] == '*' and dp[0][j - 2]:
                dp[0][j] = True

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    s = "aab"
    p = "c*a*b"
    # s = "mississippi"
    # p = "mis*is*p*."
    # s = 'aa'
    # p = 'a*'
    print(solution.isMatch(s, p))
