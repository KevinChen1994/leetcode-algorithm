# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/29 18:02

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

