# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/4 14:11

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.result = float('-inf')
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if not root:
            return 0
        left = max(self.dfs(root.left), 0)
        right = max(self.dfs(root.right), 0)
        self.result = max(self.result, root.val + left + right)
        return root.val + max(left, right)
