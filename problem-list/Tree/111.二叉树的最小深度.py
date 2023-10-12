# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/8 22:51

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and root.right:
            return 1
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        # 这里需要说明一下，如果左子树或者右子树为空，那路径肯定要选有子树的路径了，因为叶子节点的定义是没有左右子树。
        if not root.left:
            return right + 1
        if not root.right:
            return left + 1
        return min(left, right) + 1
