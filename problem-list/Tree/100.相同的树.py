# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/8 22:17

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_pre = self.preorder(p, [])
        q_pre = self.preorder(q, [])
        if p_pre == q_pre:
            return True
        else:
            return False

    def preorder(self, root, result):
        if not root:
            result.append(None)
            return result
        result.append(root.val)
        self.preorder(root.left, result)
        self.preorder(root.right, result)
        return result

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
