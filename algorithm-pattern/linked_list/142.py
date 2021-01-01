# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/13 18:24
'''
solution: 利用快慢指针，当快慢指针第一次重合时，慢指针回到第一个节点，快指针往后移动一个位置，之后快慢指针用同样的速度前进，再次相遇的节点就是环的入口。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None and head.next is None:
            return None
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            if slow == fast:
                slow = head
                fast = fast.next
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
            else:
                slow = slow.next
                fast = fast.next.next
        return None
