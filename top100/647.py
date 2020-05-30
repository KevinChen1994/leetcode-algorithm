# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/29 21:53
'''
solution: 在长度为 N 的字符串中，可能的回文串中心位置有 2N-1 个：字母，或两个字母中间。
'''
class Solution:
    def countSubstrings(self, s):
        n = len(s)
        ans = 0
        # 以某一个元素为中心的奇数长度的回文串的情况
        for center in range(n):
            left = right = center
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        # 以某对元素为中心的偶数长度的回文串的情况
        for left in range(n - 1):
            right = left + 1
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = 'abba'
    print(solution.countSubstrings(s))
