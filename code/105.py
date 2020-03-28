# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/28 21:20
# software: PyCharm
'''
solution: 两种实现方法都是递归。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree_1(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree_1(preorder[1:mid + 1], inorder[0:mid])
        root.right = self.buildTree_1(preorder[mid + 1:], inorder[mid + 1:])
        return root

    def buildTree_2(self, preorder, inorder):
        def helper(in_left=0, in_right=len(inorder)):
            nonlocal pre_idx
            if in_left == in_right:
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1
            root_node = TreeNode(root_val)
            index = idx_map[root_val]
            root_node.left = helper(in_left, index)
            root_node.right = helper(index + 1, in_right)
            return root_node

        pre_idx = 0
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()


if __name__ == '__main__':
    solution = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(solution.buildTree_2(preorder, inorder))
