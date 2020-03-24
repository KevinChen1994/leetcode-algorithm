# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/24 17:49
# software: PyCharm
'''
solution1: 递归。由观察可以得出，一棵二叉树如果是镜像树，那么这棵树的左子树与右子树镜像对称。那么两棵树如何才能判断成是镜像对称呢？
1、两棵树具有相同的根节点；2、每棵树的左子树与另外一棵树的右子树镜像对称(是的，这里又是一个递归定义)。那么就可以写出辅助函数。
solution2: 迭代。根据镜像树的定义，利用队列先进先出原则，插入队列的时候按照tree1的左子树，tree2的右子树和tree1的右子树，tree2的左子树的顺序进行插入。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def isSymmetric_1(self, root):
        return self.helper(root, root)

    def helper(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        return tree1.val == tree2.val and self.helper(tree1.left, tree2.right) and self.helper(tree1.right, tree2.left)

    def isSymmetric_2(self, root):
        queue = [root, root]
        while len(queue) != 0:
            tree1 = queue[0]
            del queue[0]
            tree2 = queue[0]
            del queue[0]
            if tree1 is None and tree2 is None:
                continue
            if tree1 is None or tree2 is None:
                return False
            if tree1.val != tree2.val:
                return False
            queue.append(tree1.left)
            queue.append(tree2.right)
            queue.append(tree1.right)
            queue.append(tree2.left)
        return True
