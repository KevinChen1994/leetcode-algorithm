# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/28 11:21

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        res = dummy
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
            else:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
        dummy.next = l1 if l1 else l2
        return res.next