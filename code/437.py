# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/19 20:36
'''
solution1: 深度优先搜索。符合条件的的总数为：以当前结点为根节点往下遍历符合条件的个数+以当前结点为的左子树根节点往下遍历符合条件的个数+
以当前结点的右子树为根节点往下遍历符合条件的个数。
在dfs中，让总数减去当前值，然后在遍历左子树和右子树就好。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):

        def dfs(root, sum):
            if root:
                sum = sum - root.val
                result = 1 if sum == 0 else 0
                return result + dfs(root.left, sum) + dfs(root.right, sum)
            else:
                return 0

        if root:
            result = dfs(root, sum)
            left = self.pathSum(root.left, sum)
            right = self.pathSum(root.right, sum)
            return result + left + right
        else:
            return 0
