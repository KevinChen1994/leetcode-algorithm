# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/20 17:31
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            queue_size = len(queue)
            tmp = []
            for i in range(queue_size):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(tmp)
        return result
