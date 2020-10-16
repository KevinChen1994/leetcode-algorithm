# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/15 17:24
'split()的时候，多个空格当成一个空格；split(' ')的时候，多个空格都要分割，每个空格分割出来空。'


class Solution:
    def reverseWords_1(self, s: str) -> str:

        s_list = s.split()
        return ' '.join(s_list[::-1])

    def reverseWords_2(self, s):
        res = ''
        s_list = s.split(' ')
        for w in s_list[::-1]:
            if w != '':
                res += w + ' '
        return res[:len(res) - 1]


solution = Solution()
s = '  hello  world!  '
print(solution.reverseWords(s))
