# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/3/3 17:59
from typing import List
'''
solution: 这道题需要用到记忆化递归来解决，使用备忘录记录下当前s所对应的所有单词切割方法，然后进行递归调用。
因为s的切法具体有多少种，取决于每一个子串有多少种切割方法，最终的答案就是一个拼接。
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordDict = wordDict
        # 使用备忘录记录每一个s对应了多少种单词切分方法
        self.mem = {}
        return self.inDict(s)

    def inDict(self, s):
        if s in self.mem:
            return self.mem[s]
        ans = []
        if s in self.wordDict:
            ans.append(s)
        for i in range(1, len(s)):
            right = s[i:]
            if right in self.wordDict:
                # 这里使用加法，是因为如果s在字典中，那么ans已经是一个列表了，存储的是就是当前s的一种切分方法
                # 要加的是另外一种切分方法，另外一种切分方法需要通过递归进行求解。
                ans += [word + ' ' + right for word in self.inDict(s[0:i])]
        self.mem[s] = ans
        return self.mem[s]


if __name__ == '__main__':
    solution = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(solution.wordBreak(s, wordDict))
