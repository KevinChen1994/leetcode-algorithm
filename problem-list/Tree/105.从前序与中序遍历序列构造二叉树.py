# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/5 14:50
from typing import List

'''
solution: 思路很简单，通过前序遍历确定根节点，通过中序遍历确定根节点的左子树和右子树。
具体代码实现，我在如何找到所有根节点困了很久，后来明白只要将前序遍历切割，每个前序遍历的第一个元素就是根节点。
切割的原则就是通过中序遍历获得左子树的长度，那么在前序遍历上获取相同的长度，这就这棵子树的全部节点。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root


if __name__ == '__main__':
    solution = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution.buildTree(preorder, inorder)
