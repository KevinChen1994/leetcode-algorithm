# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/5 23:39

class Solution:
    def replaceSpace_1(self, s: str) -> str:
        while ' ' in s:
            s = s.replace(' ', '%20')
        return s

    def replaceSpace_2(self, s):
        res = []
        for char in s:
            if char == ' ':
                res.append('%20')
            else:
                res.append(char)
        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()
    s = "We are happy."
    print(solution.replaceSpace_2(s))
