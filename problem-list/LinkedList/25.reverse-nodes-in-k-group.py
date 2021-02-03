# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/6 22:01
'''
solution: 与反转前n个链表有点类似，相对麻烦一点，需要先计算出链表的长度，然后将链表分组。

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        l = 0
        while head:
            l += 1
            head = head.next
        for i in range(l // k):
            cur = pre.next
            next = cur.next
            for j in range(1, k):
                cur.next = next.next
                next.next = pre.next
                pre.next = next
                next = cur.next
            pre = cur
        return dummy.next
