# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/4/3 16:45
# software: PyCharm
'''
solution1: 暴力法。如果s[start:end]在字典中，那么判断s[end:new_end]是否也在字典中，如果都在那么就是True
solution2: 优化的暴力法。使用memo存储进行存储结果
solution3: 动态规划。现在可以想象将字符串s分成s1和s2，如果s1、s2同时满足，那么s肯定是满足的。根据测试用例举一个例子，s='catsanddog'(这里比测试用例多了一个d)
wordDict = ["cats", "dog", "sand", "and", "cat"]，可以将s分解为'catsand'和'dog'，'catsand'又可以分解为'cats'和'and'，'cats'和'and'是存在于
字典中的，所以'catsand'满足条件，'dog'也满足条件，所以'catsandog'满足条件。这里需要注意的是，如果s1不符合条件，即代码中的dp[j]=False，那么即使s2符合条件
也是不行的，所以这里if必须两个条件都满足才可以。
'''


class Solution:
    def wordBreak_1(self, s, wordDict):

        def word_break(s, wordDict, start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict and word_break(s, wordDict, end):
                    return True
            return False

        return word_break(s, wordDict, 0)

    def wordBreak_2(self, s, wordDict):

        def word_break(s, wordDict, start, memo):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict and word_break(s, wordDict, end, memo):
                    memo[start] = True
                    return memo[start]
            memo[start] = False
            return memo[start]

        return word_break(s, wordDict, 0, {})

    def wordBreak_3(self, s, wordDict):
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
    # s = "leetcode"
    # wordDict = ["leet", "top100"]
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(solution.wordBreak_3(s, wordDict))
