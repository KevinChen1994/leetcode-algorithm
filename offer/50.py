# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/10 16:11
'''
solution: 使用字典来存储每个字符，这里不存储字符出现的次数，而是存储一个布尔类型的值。如果一个字符出现过，那么记为True，
如果再次出现，则记为False，这样只需要判断某个字符是否是True即可得到第一个不重复的字符。
'''
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = c not in dic
        for c in s:
            if dic[c]:
                return c
        return ' '




solution = Solution()
s = 'abaccdaeff'
print(solution.firstUniqChar(s))
