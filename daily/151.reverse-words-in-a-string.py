# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/25 16:04

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        n = len(s_list)
        if n == 0:
            return ''
        left = 0
        right = n - 1
        while left <= right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return ' '.join(s_list)


if __name__ == '__main__':
    solution = Solution()
    s = "  hello world!  "
    print(solution.reverseWords(s))
