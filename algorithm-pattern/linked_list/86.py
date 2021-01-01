# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/13 15:32

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before_head = ListNode(-1)
        before = before_head
        after_head = ListNode(-1)
        after = after_head
        while head:
            if head.val < x:
                before_head.next = head
                before_head = before_head.next
            else:
                after_head.next = head
                after_head = after_head.next
            head = head.next
        after_head.next = None
        before_head.next = after.next
        return before.next

