# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/7 22:54

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        res = []
        stack = [root]
        level = 0
        while stack:
            res.append([])
            level_len = len(stack)
            for i in range(level_len):
                node = stack.pop(0)
                if level % 2 == 0:
                    res[level].append(node.val)
                else:
                    res[level].insert(0, node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            level += 1

        return res
