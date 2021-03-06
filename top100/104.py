# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/26 23:27
# software: PyCharm
'''
solution: 两种深度优先遍历的实现方法
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def maxDepth_1(self, root):
        if not root:
            return 0
        else:
            left_ = self.maxDepth(root.left)
            right_ = self.maxDepth(root.right)
            return max(left_, right_) + 1

    # 迭代
    def maxDepth_2(self, root):
        stack = []
        if root:
            stack.append((1, root))
        depth = 0
        while stack:
            cur_depth, node = stack.pop()
            if node:
                depth = max(cur_depth, depth)
                stack.append((cur_depth + 1, node.left))
                stack.append((cur_depth + 1, node.right))
        return depth
