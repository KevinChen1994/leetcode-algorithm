# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/2 22:29
'''
solution: 同101
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric_1(self, root: TreeNode) -> bool:

        def helper(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None:
                return False
            return tree1.val == tree2.val and helper(tree1.left, tree2.right) and helper(tree1.right, tree2.left)

        return helper(root, root)

    def isSymmetric_2(self, root):
        from collections import deque
        queue = deque()
        queue.append((root, root))
        while queue:
            tree1, tree2 = queue.popleft()
            if tree1 is None and tree2 is None:
                continue
            if tree1 is None or tree2 is None:
                return False
            if tree1.val == tree2.val:
                queue.append((tree1.left, tree2.right))
                queue.append((tree1.right, tree2.left))
            else:
                return False
        return True

