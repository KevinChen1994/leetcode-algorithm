# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/24 16:47
'''
solution: dfs。使用深度优先搜索对每一个节点作为根节点的二叉树直径。二叉树的直径为当前节点左孩子的最大深度加上右孩子的最大深度。
注意最大直径不一定过根节点。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1

        def dfs(root):
            if not root:
                return 0
            L = dfs(root.left)
            R = dfs(root.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1

        dfs(root)
        return self.ans - 1
