# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/9 22:22
'''
solution: 由于第一个结点可能会被删除，所以需要使用dummy node作为辅助。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy_node = ListNode(-1)
        dummy_node.next = head
        a = dummy_node
        b = head.next
        while b is not None:
            if a.next.val != b.val:
                a = a.next
                b = b.next
            else:
                # 这里要先判断b是不是None，否则会报错
                while b is not None and a.next.val == b.val:
                    b = b.next
                # 把去重过的b接到a后边，b往后走一个节点，如果b是最后一个节点那么就是None，否则是下一个节点。
                a.next = b
                b = None if b is None else b.next
        return dummy_node.next

