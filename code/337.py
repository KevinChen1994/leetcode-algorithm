# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/8 20:09
'''
solution1: 暴力递归。有两个方案可以选：偷当前节点以及他的孙子节点；偷当前节点的儿子节点。对比两种方案哪个钱多选哪个。具体访问根节点的过程可以print出来看。超时。
solution2: 对solution1的优化，加了备忘录功能，从solution1的print中可以看出来，有的结点是多次访问的，那么在备忘录中将访问过的结点存储起来，就会提高效率。
solution3: 定义两种状态，当前节点偷和不偷：
1. 当前节点选择不偷：当前节点能偷到的最大钱数 = 左孩子能偷到的钱 + 右孩子能偷到的钱
2. 当前节点选择偷：当前节点能偷到的最大钱数 = 左孩子选择自己不偷时能得到的钱 + 右孩子选择不偷时能得到的钱 + 当前节点的钱数
表达成公式就是，0是不偷，1是偷
root[0] = Math.max(rob(root.left)[0], rob(root.left)[1]) + Math.max(rob(root.right)[0], rob(root.right)[1])
root[1] = rob(root.left)[0] + rob(root.right)[0] + root.val;

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob_1(self, root: TreeNode):
        if not root: return 0
        # 这里可以看出访问节点的过程
        print(root.val)
        money = root.val
        if root.left:
            money += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            money += self.rob(root.right.left) + self.rob(root.right.right)
        return max(money, self.rob(root.left) + self.rob(root.right))

    def rob_2(self, root):
        memo = {}
        def iteration(root, memo):
            if not root: return 0
            if root in memo: return memo[root]
            money = root.val
            if root.left:
                money += iteration(root.left.left, memo)+iteration(root.left.right, memo)
            if root.right:
                money += iteration(root.right.left, memo) + iteration(root.right.right, memo)
            money = max(money, iteration(root.left, memo) + iteration(root.right, memo))
            memo[root] = money
            return money
        return iteration(root, memo)

    def rob_3(self, root):

        def iteration(root):
            if not root: return [0, 0]
            result = [0, 0]
            left = iteration(root.left)
            right = iteration(root.right)
            result[0] = max(left[0], left[1]) + max(right[0], right[1])
            result[1] = root.val + left[0] + right[0]
            return result

        result = iteration(root)
        return max(result[0], result[1])