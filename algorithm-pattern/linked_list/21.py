# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/13 15:13
'''
solution1: 遍历合并
solution2: 递归，很慢
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        result = dummy
        while l1 and l2:
            if l1.val > l2.val:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
            else:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
        dummy.next = l1 if l1 else l2
        return result.next

    def mergeTwoLists_2(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        # l2比l1要小，所以将l1放到l2后边
        elif l1.val > l2.val:
            l2.next = self.mergeTwoLists_2(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists_2(l1.next, l2)
            return l1
