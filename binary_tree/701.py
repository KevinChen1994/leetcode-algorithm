# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/8 23:43
# Definition for a binary tree node.
'''
solution1: 递归
solution2: 迭代
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST_1(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    def insertIntoBST_2(self, root, val):
        node = root
        while node:
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
        # 防止输入的树是空树
        return TreeNode(val)
