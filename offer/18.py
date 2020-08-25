# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/24 18:05

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        node = head
        if node.val == val:
            return head.next
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
                break
            node = node.next
        return head