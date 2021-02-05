# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/4 15:54

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        left = left + 1 if root.left and root.val == root.left.val else 0
        right = right + 1 if root.right and root.val == root.right.val else 0
        # 判断左右子树的unipathvalue的和是否大于result的值
        self.result = max(self.result, left + right)
        # 返回的时候只能返回左右子树最大的一个unipathvalue
        return max(left, right)
