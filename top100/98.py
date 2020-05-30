# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/23 22:20
# software: PyCharm
'''
solution1: 递归，借助helper辅助函数。定义全局的最小值和最大值，当遍历根节点的左子树时，根节点为最大值；当遍历根节点的右子树时，根节点为最小值。
solution2: 迭代，DFS。使用深度优先搜索。
solution3: 利用中序遍历。搜索二叉树的中序遍历为从小到大排序的顺序，由此搜索二叉树又称为二叉排序树，可以利用这一点进行中序遍历，并比较大小。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def isValidBST_1(self, root):
        return self.helper(root)

    def helper(self, root, lower=float('-inf'), upper=float('inf')):
        if not root:
            return True
        val = root.val
        if val <= lower or val >= upper:
            return False
        if not self.helper(root.left, lower, val):
            return False
        if not self.helper(root.right, val, upper):
            return False
        return True

    # 迭代 DFS
    def isValidBST_2(self, root):
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.left, lower, val))
            stack.append((root.right, val, upper))
        return True

    # 中序遍历
    def isValidBST_3(self, root):
        stack, inoder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inoder:
                return False
            inoder = root.val
            root = root.right
        return True


if __name__ == '__main__':
    solution = Solution()
    root = [2, 1, 3]
    print(solution.isValidBST(root))
