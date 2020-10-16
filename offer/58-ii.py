# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/15 17:36

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        front = s[:n]
        back = s[n:]
        return back + front


solution = Solution()
s = 'lrloseumgh'
n = 6
print(solution.reverseLeftWords(s, n))
