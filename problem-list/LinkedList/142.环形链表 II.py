# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/29 22:54

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow != fast:
                slow = slow.next
                fast = fast.next.next
            else:
                slow = head
                fast = fast.next
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
