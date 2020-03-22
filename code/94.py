# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/21 21:50
# software: PyCharm

'''
solution1: 递归，二叉树的遍历使用递归是很简单的，操作在哪里就决定了他是什么遍历，框架如下。
>>> def traverse(TreeNode root) {
       前序遍历
>>>    traverse(root.left)
       中序遍历
>>>    traverse(root.right)
       后序遍历
}
solution2: 使用栈。在这里白色代表新节点，灰色代表已经访问过，那么也是有模板可用的。因为栈是后进先出，所以入栈的顺序与树的遍历顺序相反就好了。
# 中序遍历：
>>>if color == WHITE:
>>>    stack.append((WHITE, node.right))
>>>    stack.append((GRAY, node))
>>>    stack.append((WHITE, node.left))
>>>else:
>>>    res.append(node.val)
# 后序遍历：
>>>if color == WHITE:
>>>    stack.append((GRAY, node))
>>>    stack.append((WHITE, node.right))
>>>    stack.append((WHITE, node.left))
>>>else:
>>>    res.append(node.val)
# 先序遍历：
>>>if color == WHITE:
>>>    stack.append((WHITE, node.right))
>>>    stack.append((WHITE, node.left))
>>>    stack.append((GRAY, node))
>>>else:
>>>    res.append(node.val)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def inorderTraversal_1(self, root):
        ans = []
        if not root:
            return ans
        self.mid(root, ans)
        return ans

    def mid(self, root, ans):
        if root.left:
            self.mid(root.left, ans)
        ans.append(root.val)
        if root.right:
            self.mid(root.right, ans)

    # 使用栈
    def inorderTraversal_2(self, root):
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                # 这里如果没有右子树或者左子树，那么node.right=None
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res


if __name__ == '__main__':
    solution = Solution()
    # root = [1, 'null', 2, 3]
    root = [1, 2, 3, 4, 5, 6, 7]
    print(solution.inorderTraversal_2(root))
