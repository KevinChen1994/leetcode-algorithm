# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/6 15:36

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        for i in range(m - 1):
            head = head.next
            pre = pre.next
        for i in range(m, n):
            next = head.next
            head.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy.next
