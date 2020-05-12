# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/12 17:45
'''
solution1: 使用栈。难点在于内嵌括号，使用res存储当前遍历到的字母，num存储数字，如果遇到'['，那么将num,res进栈，并置为空和0。如果遇到']'，那么取出栈中的cur_num和last_res，
这时cur_num是[]之前的数字，last_res是[]之前的全部字母，所以使用last_res加上cur_num*累计的res，那就答案。
solution2: 递归。将[和]分别作为递归的起始条件。当遇到[时，开始进行递归，并记录[]内的字母，和最新的索引i，递归结束后，进行拼接字符串；当遇到]时，结束递归，返回[]内的字母和索引。

不得不感叹，这个代码写的是真牛逼！https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/
'''


class Solution:
    def decodeString_1(self, s):
        stack = []
        res = ''
        num = 0
        for w in s:
            if w == '[':
                stack.append((num, res))
                res, num = '', 0
            elif w == ']':
                cur_num, last_res = stack.pop()
                res = last_res + cur_num * res
            elif '0' <= w <= '9':
                # #考虑数字是2位以上的情况
                num = num * 10 + int(w)
            else:
                res += w

        return res

    def decodeString_2(self, s):
        def dfs(s, i):
            res, num = '', 0
            # 这里不能用for i in range(len(s)),因为递归调用时，新的循环不从0开始从i开始
            while i < len(s):
                if '0' <= s[i] <= '9':
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    # 注意，返回i的含义是更新上层递归指针位置，因为内层递归已经吃掉一串str，若不跟新i，外层仍然从i+1开始，则会重复处理内层处理过的一串str。
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
    s = '2[abc]3[cd]ef'
    s = '3[a2[c]]'
    print(solution.decodeString_2(s))
