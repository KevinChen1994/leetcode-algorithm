# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/25 20:50
'''
solution1: 递归。 使用深度优先遍历，如果当前节点是p或者q，那么将mid置为True，继续遍历，搜寻另外一个节点；
如果左分支或者右分支中的任何一个返回True，说明找到了两个节点中的一个；在遍历的任意一个节点上，如果left，right，mid任意两个是True，说明这个节点是最近公共祖先。
solution2: 使用父指针迭代。先找到包含p和q之前的所有节点的父节点，并存储在字典parent中。之后找到p的所有祖先，并存储在ancestor中，接着判断q的祖先是否在ancestor中出现，
第一个相同的祖先就是最近的共同祖先。
solution3: 递归的令一种写法。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor_1(self, root, p, q):

        def recurse_tree(current_node):
            if not current_node:
                return False
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            mid = current_node == p or current_node == q
            if mid + left + right >= 2:
                self.ans = current_node
            return mid or left or right

        recurse_tree(root)
        return self.ans

    def lowestCommonAncestor_2(self, root, p, q):
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node
        ancestor = set()
        while p:
            ancestor.add(p)
            p = parent[p]
        while q not in ancestor:
            q = parent[q]
        return q

    def lowestCommonAncestor_3(self, root, p, q):
        # 如果root为空或者root等于p或者q中的一个返就返回root
        if not root or p == root or q == root:
            return root
        left = self.lowestCommonAncestor_3(root.left, p, q)
        right = self.lowestCommonAncestor_3(root.right, p, q)
        if left and right:
            return root
        else:
            return left if left else right


