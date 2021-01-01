# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/6 22:34

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom_1(self, root: TreeNode):
        result = []
        if not root:
            return result
        queue = [root]
        stack = []
        while queue:
            tmp_queue = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                tmp_queue.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            stack.append(tmp_queue)
        while stack:
            queue = stack.pop()
            tmp = []
            while queue:
                node = queue.pop(0)
                tmp.append(node.val)
            result.append(tmp)
        return result

    def levelOrserBotton_2(self, root):
        result = []
        if not root:
            return result
        queue = [root]
        while queue:
            size = len(queue)
            tmp = []
            for i in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.insert(0, tmp)
        return result