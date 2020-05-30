# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/4 21:43
'''
solution: 使用BFS思想，每次在给定的s中删除一个字符，要遍历整个s,删除每个位置的一个字符，得到的新的s集合，如果是合法的，那说明找到了，
如果非法，那就继续在得到的s的集合中删除每个位置的一个字符。
'''
class Solution:
    def removeInvalidParentheses(self, s):

        def isValid(s: str) -> bool:
            cnt = 0
            for c in s:
                if c == "(":
                    cnt += 1
                elif c == ")":
                    cnt -= 1
                if cnt < 0: return False  # 只用中途cnt出现了负值，你就要终止循环，已经出现非法字符了
            return cnt == 0

        # BFS
        level = {s}  # 用set避免重复
        while True:
            valid = list(filter(isValid, level))  # 所有合法字符都筛选出来
            if valid: return valid  # 如果当前valid是非空的，说明已经有合法的产生了
            # 下一层level
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":  # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i] + item[i + 1:])
            level = next_level


if __name__ == '__main__':
    solution = Solution()
    s = '(a)())()'
    print(solution.removeInvalidParentheses(s))