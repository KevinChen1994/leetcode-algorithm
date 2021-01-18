# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/1 22:25
'''
solution: 同样是分情况讨论，与10题很类似。
1. s[i] == p[j] -> dp[i][j] = dp[i-1][j-1]
2. s[j] == ? -> dp[i][j] = dp[i-1][j-1]
3. p[j] == *
dp[i][j] = dp[i-1][j]  * means multi s[i]
or dp[i][j] = dp[i][j-1] * means empty
or dp[i][j] = dp[i-1][j-1] * means single s[i] 这种情况上边已经包含，代码里可以不写
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1 = len(s)
        l2 = len(p)
        dp = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        dp[0][0] = True
        for j in range(1, l2 + 1):
            # 这里可以直接判断p是否是以*开头的，如果不是就直接break就好。
            if p[j - 1] != '*':
                break
            if p[j - 1] == '*' and dp[0][j - 1]:
                dp[0][j] = True

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    s = "adceb"
    p = "*a*b"
    # s = "acdcb"
    # p = "a*c?b"
    print(solution.isMatch(s, p))
