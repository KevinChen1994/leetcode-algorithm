# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/8 22:28
'''
solution: 直接把leetcode-100的思路拿过来，稍微做一点变换就可以了。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.helper(root, root)

    def helper(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
