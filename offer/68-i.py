# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/26 22:14

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root

    def lowestCommonAncestor(self, root, p, q):
        # 保证q大于p
        if p.val > q.val:
            p, q = q, p
        while root:
            if p.val > root.val:
                root = root.right
            elif q.val < root.val:
                root = root.left
            else:
                return root
