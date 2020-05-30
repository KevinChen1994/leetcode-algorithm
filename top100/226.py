# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/22 22:44
'''
solution1: 递归
solution2: 迭代
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree_1(self, root: TreeNode) -> TreeNode:
        if not root: return
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

    def invertTree(self, root):
        if not root: return
        queue = [root]
        while queue:
            current = queue.pop(0)
            temp = current.left
            current.left = current.right
            current.right = temp
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root

