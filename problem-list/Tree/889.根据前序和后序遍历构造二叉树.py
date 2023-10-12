# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/5 16:35
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        # 前序遍历第二个元素是左子树的根节点，在后续遍历中这个元素在左子树遍历的最后，所以可以得到左子树的长度
        left_count = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:left_count + 1], post[0:left_count])
        root.right = self.constructFromPrePost(pre[left_count + 1:], post[left_count:-1])
        return root


if __name__ == '__main__':
    solution = Solution()
    pre = [1, 2, 4, 5, 3, 6, 7]
    post = [4, 5, 2, 6, 7, 3, 1]
    solution.constructFromPrePost(pre, post)
