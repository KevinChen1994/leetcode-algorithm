# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/12/22 11:13
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
solution: 跟使用前序遍历和中序遍历思想一样，都是使用递归。
现在从后序遍历中找到根节点，然后在中序遍历中找到根节点的索引，这样就知道了左子树有谁，右子树有谁，
直接使用递归，即可恢复这棵树。
'''

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index:-1])
        return root


if __name__ == '__main__':
    solution = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    solution.buildTree(inorder, postorder)
