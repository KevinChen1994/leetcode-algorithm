# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/4/1 22:43
# software: PyCharm
'''
solution: 使用递归的思想。定义一个helper辅助函数，返回当前值与左子树和右子树最大的那个的值，
在helper中递归调用helper，同时记录最大路径和，那么最大的路径和就是一个节点加上左右两边最大的节点(也有可能什么都不加)
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        max_sum = float('-inf')

        def helper(node):
            nonlocal max_sum
            if not node:
                return 0
            # 防止有负数出现
            left_ = max(helper(node.left), 0)
            right_ = max(helper(node.right), 0)

            cur_sum = node.val + left_ + right_

            max_sum = max(max_sum, cur_sum)
            # 这里返回只能返回左子树或者右子树其中一个，因为一个节点只能用一次，左子树和右子树都返回的话，
            # 他们与根节点就不能再与其他的节点相连，否则根节点就使用了两次。
            return node.val + max(left_, right_)

        helper(root)
        return max_sum
