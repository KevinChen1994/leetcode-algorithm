# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/21 15:47
'''
solution: 使用dfs回溯加剪枝；思想主要是固定住前n位，后边进行交换，同时使用set进行记录已经固定的字母，如果遇到相同的字母，那就跳过，
这个操作为剪枝。
递归是真的头疼。。。总是感觉理解了又差点意思。
'''
class Solution:
    def permutation(self, s: str):
        c, res = list(s), []

        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic:
                    continue
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]
                print(c)
                dfs(x + 1)
                c[i], c[x] = c[x], c[i]

        dfs(0)
        return res


if __name__ == '__main__':
    solution = Solution()
    s = 'abc'
    print(solution.permutation(s))
