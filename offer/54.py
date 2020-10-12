# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/12 17:10
'''
solution: 因为是二叉搜索树，所以中序遍历的结果就是有小到大排序。这里需要将中序遍历反过来，即：先右子树，再根节点，最后左子树即可。
在遍历过程中，使用res记录结果，但是遍历不是全部遍历，而是统计遍历次数，只遍历k个结点即可。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.inorder(root)
        return self.res

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.right)
        if self.k == 0:
            return
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.inorder(root.left)
