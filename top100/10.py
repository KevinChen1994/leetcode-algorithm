# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/1/14 16:04
# software: PyCharm
import re


class Solution:
    # 作弊的方法，直接调用re库，88 ms
    def isMatch_1(self, s, p):
        return True if s in re.findall(p, s, flags=0) else False

    # 递归，占用时间比较长，1792 ms
    def isMatch_2(self, s, p):
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        # 如果正则中包含*，有两种选项：1是直接忽略*，也就是*在这里匹配0次；2匹配*前一个字符一次，然后移动字符串s一个位置，继续递归
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch_2(s, p[2:]) or first_match and self.isMatch_2(s[1:], p)
        else:
            return first_match and self.isMatch_2(s[1:], p[1:])

    # 对方法2的优化，避免重复计算，降低复杂度，64 ms
    def isMatch_3(self, s, p):
        memo = dict()  # 备忘录

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)

            first = i < len(s) and p[j] in {s[i], '.'}

            if j <= len(p) - 2 and p[j + 1] == '*':
                ans = dp(i, j + 2) or first and dp(i + 1, j)
            else:
                ans = first and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch_3('aab', 'c*a*b'))
