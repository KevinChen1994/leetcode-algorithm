# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/8 20:10
'''
solution: 使用dfs，关于target在回溯时要不要加回减去的值：因为回溯是回到上一层遍历，而target是值传递，所以上一层遍历中还存有上一次的target，
所以不需要在加回来。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        res, path = [], []

        def helper(root, target):
            if not root:
                return
            path.append(root.val)
            target -= root.val
            if target == 0 and not root.left and not root.right:
                # 直接append path的话，后续path会影响到这个值，这是地址传递，不是值传递
                res.append(path[:])
            helper(root.left, target)
            helper(root.right, target)
            # 此路径不满足要求，弹出最后一个节点，进行回溯
            path.pop()

        helper(root, sum)
        return res
