# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/1 23:15
from typing import List
'''
solution: 使用层次遍历，每一层将队列最后一个元素放到结果中，就是最右边的那个元素。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        queue = [root]
        while queue:
            n = len(queue)
            result.append(queue[-1].val)
            for i in range(n):
                root = queue.pop(0)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return result
