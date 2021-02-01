# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/1 22:29
'''
solution: 因为是二叉搜索树，所以每个节点都大于其左子树且小于其右子树，这样就可以通过判断两个节点与当前节点的大小来判断祖先节点在哪里。
如果当前节点大于两个节点，那么说明这两个节点都在当前节点左边，且当前节点不是祖先节点；
如果当前节点小于两个节点，那么说明这两个节点都在当前节点右边，且当前节点不是祖先节点；
否则，两个节点分布在当前节点的左右两边，当前节点也就是最近的公共祖先。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            self.lowestCommonAncestor(root.right, p, q)
        return root