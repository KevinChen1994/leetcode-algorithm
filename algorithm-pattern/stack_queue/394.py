# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/14 18:14
'''
solution1: 使用栈存储要翻的倍数和翻倍之前的结果。
solution2: 递归。
'''


class Solution:
    def decodeString_1(self, s: str) -> str:
        num = 0
        result = ''
        stack = []
        for w in s:
            if '0' <= w <= '9':
                num = num * 10 + int(w)
            elif w == '[':
                stack.append([num, result])
                num = 0
                result = ''
            elif w == ']':
                cur_num, last_res = stack.pop()
                result = last_res + cur_num * result
            else:
                result += w
        return result

    def decodeString_2(self, s):
        def dfs(s, i):
            res, num = '', 0
            # 这里不能用for i in range(len(s)),因为递归调用时，新的循环不从0开始从i开始
            while i < len(s):
                if '0' <= s[i] <= '9':
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    # 注意，返回i的含义是更新上层递归指针位置，因为内层递归已经吃掉一串str，若不更新i，外层仍然从i+1开始，则会重复处理内层处理过的一串str。
                    i, tmp = dfs(s, i + 1)
                    res += num * tmp
                    num = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(s, 0)


if __name__ == '__main__':
    solution = Solution()
    s = '3[a2[c]]'
    print(solution.decodeString_1(s))
