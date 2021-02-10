# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/10 23:01

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return True
        if not root.left and root.right:
            return root.val == root.right.val and self.isUnivalTree(root.right)
        if not root.right and root.left:
            return root.val == root.left.val and self.isUnivalTree(root.left)
        return root.val == root.left.val == root.right.val and self.isUnivalTree(root.left) and self.isUnivalTree(
            root.right)

    def isUnivalTree(self, root: TreeNode) -> bool:
        self.values = []
        self.preOrder(root)
        return True if sum(self.values) / len(self.values) == self.values[0] else False

    def preOrder(self, root):
        if not root:
            return
        self.values.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
