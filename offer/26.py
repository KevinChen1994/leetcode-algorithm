# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/1 21:54
'''
solution: 方法1写的相对比较简洁，方法2是方法1的详细写法。思路就是在遍历过程中进行判断。
首先如果A或者B有空的话，那肯定是False。定义一个辅助函数，用来判断两棵树是否是子树，这个函数需要判断：如果B是空，说明是子树，因为前边已经进行过B的判空了，
这里是空，说明B的全部节点已经都判断过了；如果A是空，那就不是子树了，因为B还有，A就没了，肯定不行的；另外需要满足A的左子树和B的左子树，A的右子树和B的右子树
也是符合子树的定义的。定义好辅助函数，在主函数里就需要判断，A和B是不是子树关系，不是没关系，看A的左子树和B是不是子树关系，或者A的右子树和B是不是子树关系，
只要其中有个满足就可以。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure_1(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure_1(A.left, B) or self.isSubStructure_1(A.right, B))

    def isSubTree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        if A.val == B.val:
            return self.isSubTree(A.left, B.left) and self.isSubTree(A.right, B.right)

    def isSubStructure_2(self, A, B):
        if not A or not B:
            return False
        return self.isSubTree(A, B) or self.isSubStructure_2(A.left, B) or self.isSubStructure_2(A.right, B)
