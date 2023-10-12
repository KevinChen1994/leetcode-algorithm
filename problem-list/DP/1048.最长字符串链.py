# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/3/6 21:35
from typing import List
'''
solution: 思路是比较清晰的，使用dp去记录每一个位置能构成的最长字符串链。
需要实现一个判断两个字符串是否是词链，规则就是如果两个字符串长度相差不是1，那肯定不是；
如果长度相差1，那么通过两个指针分别指向两个字符串，相同就同时移动一位，不同的话，长的那个就移动一位，最后看短的字符串指针的长度就好。
'''

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_sorted = sorted(words, key=lambda x: len(x), reverse=False)
        n = len(words_sorted)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if self.check(words_sorted[i], words_sorted[j]):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    def check(self, word1, word2):
        if len(word1) - len(word2) != 1:
            return False
        p1 = 0
        p2 = 0
        while p1 < len(word1) and p2 < len(word2):
            if word1[p1] == word2[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 += 1
        if p2 == len(word2):
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    print(solution.longestStrChain(words))
