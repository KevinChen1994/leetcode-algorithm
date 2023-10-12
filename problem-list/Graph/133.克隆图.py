# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/28 11:10
'''
solution: 使用dfs遍历整个图，然后将每个结点存储到字典中，构建一个新的图。
'''


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


# adjList = [[2,4],[1,3],[2,4],[1,3]]
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.lookup = {}
        return self.dfs(node)

    def dfs(self, node):
        if not node:
            return node
        if node in self.lookup:
            return self.lookup[node]
        clone = Node(node.val, [])
        self.lookup[node] = clone
        for n in node.neighbors:
            clone.neighbors.append(self.dfs(n))
        return clone


if __name__ == '__main__':
    solution = Solution()
    ns = [Node(i, []) for i in range(0, 5)]
    ns[1].neighbors = [ns[2], ns[4]]
    ns[2].neighbors = [ns[1], ns[3]]
    ns[3].neighbors = [ns[2], ns[4]]
    ns[4].neighbors = [ns[3], ns[1]]

    res = solution.cloneGraph(ns[1])
    print(res)
