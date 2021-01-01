# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/28 22:55
'''
solution: 初始化dp数组全为false，并且有n+1个，因为第一个要初始化为True，dp[i]代表前i个元素可以拆分为字典中的词。在遍历过程中，考虑如下问题，以当前元素为i终点，
以i之前的任意位置j为起点是否在字典中，并且dp[j]是否为True，如果dp[j]为True，说明前j个元素可以用字典表示，并且s[j:i]也在字典中，说明前i个元素可以用字典表示。
'''
class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]


if __name__ == '__main__':
    solution = Solution()
    s = 'applepenapple'
    wordDict = ["apple", "pen"]
    print(solution.wordBreak(s, wordDict))
