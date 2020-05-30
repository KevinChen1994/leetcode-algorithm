#-*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/29 22:26
# software: PyCharm
'''
solution1: 流程：1、将右子树放到左子树最右边的节点；2、将左子树放到右子树的位置；3、root变成右子树
solution2: 其实题目要求可以理解为是将二叉树改为按照前序遍历的顺序在右子树排列。那么就可以考虑使用前序遍历，如果使用递归的话，
左子树的值赋值到右子树，就会丢失掉右子树的数据，这里可以使用栈来存储右子树的数据。利用栈实现二叉树的前序遍历。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten_1(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if not root.left:
                root = root.right
            else:
                # 找到左子树最右边的节点
                pre = root.left
                while pre:
                    if pre.right:
                        pre = pre.right
                    else:
                        break
                # 将原来的树的右子树放到左子树最右边的节点
                pre.right = root.right
                # 将左子树放到右子树的位置
                root.right = root.left
                root.left = None
                root = root.right

    def flatten_2(self, root):
        if not root:
            return
        stack = [root]
        res = TreeNode(0)
        while stack:
            temp = stack.pop()
            res.right = temp
            res.left = None
            res = res.right
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        root = res.right




