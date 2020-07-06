# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/6 23:03
'''
solution: 设置一个flag，是True的时候就将结果从左到右输出到数组中，False的话就从右到左输出到数组中。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        result = []
        if not root:
            return result
        queue = [root]
        flag = True
        while queue:
            tmp = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if flag:
                    tmp.append(node.val)
                else:
                    tmp.insert(0, node.val)
            flag = False if flag else True
            result.append(tmp)
        return result

