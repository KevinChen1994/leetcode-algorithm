# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/19 20:36
'''
solution1: 深度优先搜索。符合条件的的总数为：以当前结点为根节点往下遍历符合条件的个数+以当前结点为的左子树根节点往下遍历符合条件的个数+
以当前结点的右子树为根节点往下遍历符合条件的个数。
在dfs中，让总数减去当前值，然后在遍历左子树和右子树就好。
solution2: dfs。累计记录路径之和，并在字典中存储每个路径和，使用当前路径和减去sum，剩余的这个数如果在字典中出现，那么就相当于找到了符合条件的路径。
有点tricky，这个方法太难想了。但是速度极快。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum_1(self, root: TreeNode, sum: int):

        def dfs(root, sum):
            if root:
                sum = sum - root.val
                result = 1 if sum == 0 else 0
                return result + dfs(root.left, sum) + dfs(root.right, sum)
            else:
                return 0

        if root:
            result = dfs(root, sum)
            left = self.pathSum(root.left, sum)
            right = self.pathSum(root.right, sum)
            return result + left + right
        else:
            return 0

    def dfs(self, root, sum, prefixSum, currSum):
        if not root:
            return 0
        res = 0
        currSum += root.val
        residule = currSum - sum
        # 记录路径上的结点之和，然后用路径和减去sum,得到一个剩余的数residule,如果结点上有这个数，说明这条路径是符合要求的。
        # 因为只要将剩余的那个和的结点减去就是我们要的sum.
        res += prefixSum[residule]
        prefixSum[currSum] += 1
        res += self.dfs(root.left, sum, prefixSum, currSum)
        res += self.dfs(root.right, sum, prefixSum, currSum)
        prefixSum[currSum] -= 1
        return res

    def pathSum_2(self, root, sum):
        from collections import defaultdict
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        return self.dfs(root, sum, prefixSum, 0)
