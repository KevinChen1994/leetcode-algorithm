# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/8 15:22

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        while head.next:
            next = head.next
            head.next = next.next
            next.next = dummy.next
            dummy.next = next
        return dummy.next