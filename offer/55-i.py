# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/13 22:51
'''
solution1: 递归DFS
solution2: 迭代DFS
solution3: BFS
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth_1(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left, right) + 1

    def maxDepth_2(self, root):
        stack = []
        if root:
            stack.append((1, root))
        depth = 0
        while stack:
            cur_depth, node = stack.pop()
            if node:
                depth = max(depth, cur_depth)
                stack.append((cur_depth + 1, node.left))
                stack.append((cur_depth + 1, node.right))
        return depth

    def maxDepth_3(self, root):
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            depth += 1
        return depth
