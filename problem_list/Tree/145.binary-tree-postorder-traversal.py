# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/19 14:12
from typing import List
'''
solution1: 使用辅助栈，与前序和中序不同的是，答案依次插入数组头部
solution2: 递归
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            root = stack.pop()
            result.insert(0, root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return result

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []
        self.postorder(root)
        return self.result

    def postorder(self, root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.result.append(root.val)
