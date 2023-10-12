# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/4 11:13

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.ans = max(self.ans, left + right)
        return max(left, right) + 1
