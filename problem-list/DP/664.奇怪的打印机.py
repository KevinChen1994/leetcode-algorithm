'''
很明显是动态规划的题目，难在如何定义状态转矩矩阵。
通过观察case可以看出，如果只有一个字母，那就是打印一次；
如果有两个字母，需要判断两个字母是否一致，一致的话打印一次，不一致打印两次；
如果有三个字母，需要判断三个字母是否一致，如果一致打印一次，如果开头和结尾一致，则打印两次；
比如aba，可以先打印出aaa，再打印aba，从这里可以看出打印aba的次数等于打印ab的次数（容易观察到，但不容易注意到）；
那定义dp[i][j]表示打印从索引i到j打印的最少次数，
从上边的观察可以得出：如果只有一个字母dp[i][j] = 1，如果大于1，则判断开头结尾是否一致，一致的话，dp[i][j] = dp[i][j - 1]
如果不一致的话，则需要遍历所有的情况，选择最小的。
'''

class Solution:
    def strangePrinter(self, s: str) -> int:
        dp = [[float('inf')] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                if (s[i] == s[j]):
                    dp[i][j] = dp[i][j - 1]
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        return dp[0][-1]

if __name__ == '__main__':
    solution = Solution()
    s = "abab"
    res = solution.strangePrinter(s)
    print(res)