# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/4 13:59
'''
solution: dp[i][j]代表s1[0:i]与s2[0:j]能交错构成s3[0:i+j]
需要提前设置好边界，dp[0][0] = True，
如果s1的前i个与s3的前i个相同，dp[0...i][0] = True,
如果s2的前j个与s3的前j个相同，dp[0][0...j] = True
转移方程需要考虑s1与s2中的字符谁先来作为s3的子串，所以将他们融合到一起写，
如果dp[i-1][j]=True，并且s1[i-1] == s3[i+j-1]，也就是说s3的下一个子串由s1的第i字符来充当，并且s1[0:i-1]与s2[0:j]能交错构成s3[0:i+j-1]
同理，s2也可以使用同样的方法来判断。两个方法哪个适用就采用哪个，如果都不适用，那就是False
'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False
        dp = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        dp[0][0] = True
        for i in range(1, l1 + 1):
            if s1[i - 1] != s3[i - 1]:
                break
            dp[i][0] = True
        for j in range(1, l2 + 1):
            if s2[j - 1] != s3[j - 1]:
                break
            dp[0][j] = True
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    # s1 = "aabcc"
    # s2 = "dbbca"
    # s3 = "aadbbcbcac"
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    print(solution.isInterleave(s1, s2, s3))
