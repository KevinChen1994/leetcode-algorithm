# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/15 22:30

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            # pre用来存储当前节点左边的结点
            # 如果pre存在，那么pre右边就是当前节点，当前节点左边就是pre
            if self.pre:
                self.pre.right = root
                root.left = self.pre
            else:
                # 如果pre不存在，说明现在的结点是第一个节点，使用head进行存储。
                self.head = root
            # 将pre与当前节点左右都连接好后，当前节点变成pre，相当于指针右移
            self.pre = root
            in_order(root.right)

        if not root:
            return
        self.pre = None
        in_order(root)
        # 所有结点都左右连接好了，这时要将第一个节点与最后一个节点连接形成环
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head
