# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/8 16:08
'''
solution1: 递归调用validBST函数，如果是左子树，那么high就是根节点；如果是右子树，那么low就是根节点。
solution2: 利用中序遍历。BST的特性就是中序遍历的结果是有小到大的数。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST_1(self, root: TreeNode) -> bool:
        return self.validBST(root)

    def validBST(self, root, low=float('-inf'), high=float('inf')):
        if not root:
            return True
        val = root.val
        if val <= low or val >= high:
            return False
        if not self.validBST(root.left, low, val):
            return False
        if not self.validBST(root.right, val, high):
            return False
        return True

    def isValidBST_2(self, root):
        if not root:
            return True
        stack = []
        tmp = float('-inf')
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                val = root.val
                root = root.right
                if val > tmp:
                    tmp = val
                else:
                    return False
        return True

