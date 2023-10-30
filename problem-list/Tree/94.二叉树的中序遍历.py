# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/19 13:13
from typing import List
'''
solution1: 使用栈进行迭代
solution2: 递归
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []
        self.inorder(root)
        return self.result

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.result.append(root.val)
        self.inorder(root.right)

if __name__ == '__main__':
    left = TreeNode('B')
    right = TreeNode('C')
    tree = TreeNode('A')
    tree.left = left
    tree.right = right
    solution = Solution()
    res = solution.inorderTraversal(tree)