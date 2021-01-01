# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/3 22:21
'''
solution1: 高度平衡二叉树需要满足：左子树是高度平衡二叉树；右子树是高度平衡二叉树；左右子树深度差值不能大于1.
isBalanced()会遍历整个二叉树，时间复杂度是O(N),depth()需要遍历各子树的所有结点，时间复杂度是O(logN),
所以最终时间复杂度是O(NlogN)
solution2: 使用一个全局变量记录状态，如果有一棵子树不是高度平衡二叉树，那么整个数也就不是。需要遍历整个子树，
时间复杂度为O(N)
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced_1(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isBalanced_1(root.left) and self.isBalanced_1(root.right) and abs(
            self.depth(root.left) - self.depth(root.right)) <= 1

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    def isBalanced_2(self, root):
        self.result = True
        self.max_depth(root)
        return self.result

    def max_depth(self, root):
        if not root:
            return 0
        left = self.max_depth(root.left)
        right = self.max_depth(root.right)
        if abs(left - right) > 1:
            self.result = False
        return max(left, right) + 1
