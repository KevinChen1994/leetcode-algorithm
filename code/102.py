# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/25 18:12
# software: PyCharm
'''
solution1: 递归。
solution2: 迭代。
两个思路基本都差不多，都是广度优先遍历，都有一个level用来记录当前遍历到第几层。
'''

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def levelOrder_1(self, root):
        ans = []
        if not root:
            return ans
        self.helper(root, ans, 0)
        return ans

    def helper(self, node, ans, level):
        if len(ans) == level:
            ans.append([])
        ans[level].append(node.val)
        if node.left:
            self.helper(node.left, ans, level + 1)
        if node.right:
            self.helper(node.right, ans, level + 1)

    # 迭代
    def levelOrder_2(self, root):
        ans = []
        if not root:
            return ans
        level = 0
        queue = deque([root])
        while queue:
            ans.append([])
            level_len = len(queue)
            for i in range(level_len):
                node = queue.popleft()
                ans[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return ans
