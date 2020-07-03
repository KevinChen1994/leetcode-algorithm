# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/6/29 15:11
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def maxDepth_1(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left = self.maxDepth_1(root.left)
            right = self.maxDepth_1(root.right)
            return max(left, right) + 1

    # 迭代
    def maxDepth_2(self, root):
        stack = []
        if root:
            stack.append((root, 1))
        max_depth = 0
        while stack:
            root, cur_depth = stack.pop()
            if root:
                max_depth = max(cur_depth, max_depth)
                stack.append((root.left, cur_depth + 1))
                stack.append((root.right, cur_depth + 1))
        return max_depth
