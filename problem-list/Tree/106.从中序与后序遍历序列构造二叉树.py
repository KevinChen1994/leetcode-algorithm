# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/5 15:41
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid: -1])
        return root


if __name__ == '__main__':
    solution = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    solution.buildTree(inorder, postorder)
