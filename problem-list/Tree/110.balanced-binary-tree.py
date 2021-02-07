# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/7 14:46

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.result = True
        self.depth(root)
        return self.result

    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.left)
        if abs(left - right) > 1:
            self.result = False
        return max(left + right) + 1
