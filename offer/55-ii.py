# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/13 23:19
'''
solution1: 先序遍历（迭代）+判断深度
solution2: 先序遍历（递归）+深度判断
solution3: 后续遍历+剪枝。从下往上进行查找，分别求出左子树与右子树的深度，然后计算。
https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/solution/mian-shi-ti-55-ii-ping-heng-er-cha-shu-cong-di-zhi/
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
        queue = [root]
        while queue:
            node = queue.pop(0)
            if abs(self.cal_depth(node.left) - self.cal_depth(node.right)) > 1:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True

    def cal_depth(self, node):
        if not node:
            return 0
        left = self.cal_depth(node.left)
        right = self.cal_depth(node.right)
        return max(left, right) + 1

    def isBalanced_2(self, root):
        if not root:
            return True
        return abs(self.cal_depth(root.left) - self.cal_depth(root.right)) <= 1 and self.isBalanced_2(
            root.left) and self.isBalanced_2(root.right)

    def isBalanced_3(self, root):
        def recur(node):
            if not node:
                return 0
            left = recur(node.left)
            if left == -1:
                return -1
            right = recur(node.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1
