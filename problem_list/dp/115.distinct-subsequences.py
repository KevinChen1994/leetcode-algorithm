# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/4 16:14
'''
solution: 定义dp[i][j]为s[0:i]与t[0:j]的匹配次数。
首先定义初始状态，先全部定义为0，如果t为空，那么s为任意值都能匹配，所以将dp[i][0]定义为1。
状态转移：如果s[i-1]与t[j-1]相等，那么dp[i][j]的值为，s[0:i-1]与t[0:j-1]的匹配次数，也就是dp[i-1][j-1]，
加上s[0:i-1]与t[0:j]的次数。举例说明：baba与ba，最后的两个a相等，bab与b的次数为2，bab与ba的次数为1，那么
baba与ba的次数为2+1=3。
如果s[i-1]与t[j-1]不相等，那么dp[i][j]的值为，去掉s[i-1]后的值。
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1 = len(s)
        l2 = len(t)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(l1 + 1):
            dp[i][0] = 1
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    s = "babgbag"
    t = "bag"
    print(solution.numDistinct(s, t))
