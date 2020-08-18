# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/11 23:01
'''
solution: 根据前序遍历可以确定根节点，根据中序遍历可以确定左子树和右子树，根据这个特性，肯定是使用递归来处理。
有一种暴力的解法在105中，这种解法借助了字典来存储中序遍历中每一个元素的位置，理解起来不难，但是很难想到这个解法。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        self.dict, self.preorder = {}, preorder
        # 使用字典记录中序遍历中每一个元素的位置
        for i in range(len(inorder)):
            self.dict[inorder[i]] = i
        return self.recur(0, 0, len(inorder) - 1)

    # pre_root 前序遍历中根节点索引，in_left中序遍历左边界，in_right中序遍历右边界
    def recur(self, pre_root, in_left, in_right):
        # 终止条件，中序遍历为空
        if in_left > in_right:
            return
        # 建立当前子树的根节点
        root = TreeNode(self.preorder[pre_root])
        # 搜索根节点在中序遍历中的索引，从而可对根节点、左子树、右子树进行划分
        i = self.dict[self.preorder[pre_root]]
        root.left = self.recur(pre_root + 1, in_left, i - 1)
        # i - in_left + pre_root + 1为根节点索引+左子树长度+1
        root.right = self.recur(i - in_left + pre_root + 1, i + 1, in_right)
        return root
