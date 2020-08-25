# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/24 18:10

class Solution:
    def isMatch_1(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                # 正则为空或者正则不为空的两种情况
                if j == 0:
                    # 如果正则为空，并且字符串也为空，那么可以匹配
                    dp[i][j] = i == 0
                else:
                    # 非空正则分为*和非*
                    if p[j - 1] != '*':
                        # 如果正则上一个字符不是*，那就判断字符串上一个字符与正则上一个字符是相等或者正则上一个字符是否为.，.可以匹配任意字符
                        if i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '.'):
                            dp[i][j] = dp[i - 1][j - 1]
                    else:
                        # 如果正则上一个字符为*，那么正则前两个字符c，可以匹配0或多次。那就分情况讨论：
                        if j >= 2:
                            # |按位或，有一个1就是1。这里匹配的是c出现0次。
                            dp[i][j] |= dp[i][j - 2]
                        # 如果字符串上一个与正则的上两个相等，或者正则上两个是.，那么当前是否能匹配取决了字符串上一个。
                        if i >= 1 and j >= 2 and (s[i - 1] == p[j - 2] or p[j - 2] == '.'):
                            dp[i][j] |= dp[i - 1][j]
        return dp[-1][-1]

    def isMatch_2(self, s, p):
        memo = dict()  # 备忘录

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            # 如果正则这个字符等于字符串的字符，或者正则是.
            first = i < len(s) and p[j] in {s[i], '.'}

            if j <= len(p) - 2 and p[j + 1] == '*':
                ans = dp(i, j + 2) or first and dp(i + 1, j)
            else:
                ans = first and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)


if __name__ == '__main__':
    solution = Solution()
    s = 'aab'
    p = 'c*a*b'
    print(solution.isMatch(s, p))
