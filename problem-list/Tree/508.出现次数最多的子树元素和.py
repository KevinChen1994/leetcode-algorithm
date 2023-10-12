# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/4 22:48
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        from collections import defaultdict
        self.dict = defaultdict(int)
        self.dfs(root)
        if sum(self.dict.values()) == len(self.dict):
            return list(self.dict.keys())
        max_value = max(self.dict.values())
        return [key for key, value in self.dict.items() if value == max_value]

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.dict[root.val + left + right] += 1
        return root.val + left + right
