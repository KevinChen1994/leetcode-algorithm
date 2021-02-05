# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/5 22:45
from typing import List
'''
solution: 这道题跟leetcode-449一样
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(low=float('-inf'), high=float('inf')):
            if not preorder or preorder[0] < low or preorder[0] > high:
                return None
            val = preorder.pop(0)
            root = TreeNode(val)
            root.left = helper(low, val)
            root.right = helper(val, high)
            return root

        return helper()


if __name__ == '__main__':
    solution = Solution()
    preorder = [8, 5, 1, 7, 10, 12]
    solution.bstFromPreorder(preorder)
