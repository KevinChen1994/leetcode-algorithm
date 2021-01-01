# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/4 22:06

'''
solution: 分治思想，递归计算出左右节点分别的贡献值，只有当贡献值大于0时才使用这条路径。结点的贡献值取决于当前结点的值和他的左右节点的贡献值，每次递归返回该节点的最大贡献值。时间复杂度O(N)，对每个节点只访问一次。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_result = float('-inf')
        self.maxContribution(root)
        return self.max_result

    # 返回结点的最大贡献值，并且在遍历过程中记录最大的路径和
    def maxContribution(self, root):
        if not root:
            return 0
        # 只保留左右节点大于0的贡献值。
        left = max(self.maxContribution(root.left), 0)
        right = max(self.maxContribution(root.right), 0)
        # 节点路径和取决于当前节点和他左右节点的最大贡献值
        self.max_result = max(self.max_result, root.val + left + right)
        # 返回该节点的贡献值
        return root.val + max(left, right)
