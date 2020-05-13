# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/13 17:02
'''
solution1: 图+dfs。先构建一个图，图的结构是graph[x][y]=v，那么就是x/y=v。然后通过dfs进行递归遍历图，最终的结果是图上路径的乘积。看一下注释就清楚了。

'''

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}
        for (x, y), v in zip(equations, values):
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y: v}
            if y in graph:
                graph[y][x] = 1 / v
            else:
                graph[y] = {x: 1 / v}

        # dfs找寻从s到t的路径并返回结果叠乘后的边权重即结果
        def dfs(s, t):
            if s not in graph:
                return -1
            if s == t:
                return 1
            for node in graph[s].keys():
                if node == t:
                    return graph[s][node]
                elif node not in visited:
                    visited.add(node)
                    v = dfs(node, t)
                    if v != -1:
                        # 这里举个例子：例如要求a/c，那么现在只有a/b=2,b/c=3，那么a/c=a/b*b/c=6
                        return graph[s][node] * v
            return -1

        res = []
        for qs, qt in queries:
            visited = set()
            res.append(dfs(qs, qt))
        return res


if __name__ == '__main__':
    solution = Solution()
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    # [6.0, 0.5, -1.0, 1.0, -1.0 ]
    print(solution.calcEquation(equations, values, queries))
