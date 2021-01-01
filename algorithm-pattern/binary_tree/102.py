# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/6 21:49
'''
solution: 使用队列记录每一层的节点，遍历当前队列的大小次，每次遍历当前队列中的节点。一个数进去一次出来一次，时间复杂度O(logN)
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        result = []
        if not root:
            return result
        queue = [root]
        while queue:
            tmp_list = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                tmp_list.append(node.val)
            result.append(tmp_list)
        return result
