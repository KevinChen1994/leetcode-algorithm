# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/2/24 15:42
# software: PyCharm

class Solution:
    def isValid(self, s):
        key_map = {'(': ')', '{': '}', '[': ']', ')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            else:
                if stack[-1] == key_map[i]:
                    stack.pop()
                else:
                    stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('({})[]'))
