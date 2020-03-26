# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/26 23:27
# software: PyCharm

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


