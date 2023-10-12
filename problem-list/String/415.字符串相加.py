# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/1 22:48
'''
solution: 这道题用二进制算会更快，但是我实在不想搞二进制。
这道题要返回的是字符串，不是数字，写的时候差点弄错了。
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ''
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0 or carry != 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            i, j = i - 1, j - 1
            result = str(tmp % 10) + result
        return result


if __name__ == '__main__':
    solution = Solution()
    num1 = '123'
    num2 = '8888'
    print(solution.addStrings(num1, num2))
