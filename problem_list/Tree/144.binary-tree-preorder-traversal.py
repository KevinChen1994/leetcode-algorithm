# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/19 13:56
from typing import List
'''
solution1: 利用栈进行迭代
solution2: 递归
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left


#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        while root or stack:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return result

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []
        self.preorder(root)
        return self.result

    def preorder(self, root):
        if not root:
            return
        self.result.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
