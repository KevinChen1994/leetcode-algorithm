# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/23 20:22
'''
搜索二叉树，左子树的结点均小于根节点，右子树的结点均大于等于根节点
solution1: 反序中序遍历
solution2: 利用栈，不进行递归
solution3: 反序中序 Morris 遍历，将空间复杂度压缩到了常数
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.total = 0

    def convertBST_1(self, root):
        if root:
            self.convertBST_1(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST_1(root.left)
        return root

    def converBST_2(self, root):
        total = 0
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
        return root

    def covertBST_3(self, root):
        def get_Successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ

        total = 0
        node = root
        while node is not None:
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            else:
                succ = get_Successor(node)
                if succ.left is None:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        return root