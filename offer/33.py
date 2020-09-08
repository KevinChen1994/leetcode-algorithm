# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/8 19:15
'''
solution1: 搜索二叉树的后续遍历最后一个元素就是根节点，在搜索二叉树中，根节点大于左子树的所有结点，小于右子树的所有结点。
所以先通过根节点划分左子树和右子树，然后通过递归去判断。判断的过程为根据搜索二叉树的性质，可以从后续遍历的开始一直到结束，只要符合这个过程就可以。
solution2: 使用单调栈，我是实在没看懂。https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/
'''


class Solution:
    def verifyPostorder_1(self, postorder) -> bool:

        def helper(i, j):
            if i >= j:
                return True
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            return p == j and helper(i, m - 1) and helper(m, j - 1)

        return helper(0, len(postorder) - 1)

    def verifyPostorder_2(self, postorder):
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while (stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True


if __name__ == '__main__':
    solution = Solution()
    postorder = [1, 3, 2, 6, 5]
    print(solution.verifyPostorder_2(postorder))
