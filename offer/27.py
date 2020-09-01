# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/1 22:46

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree_1(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = self.mirrorTree_1(root.right), self.mirrorTree_1(root.left)
        return root

    def mirrorTree_2(self, root):
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root