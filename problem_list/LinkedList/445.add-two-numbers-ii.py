# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/8 15:53
'''
solution: 如果翻转链表的话，那跟lc2就是一道题，这里用了不翻转的方法。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(-1)
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        ten = 0
        while stack1 or stack2 or ten:
            sum = stack1[-1] if stack1 else 0
            sum += stack2[-1] if stack2 else 0
            sum += ten
            if stack1:
                stack1.pop()
            if stack2:
                stack2.pop()
            ten = sum // 10
            new_node = ListNode(sum % 10)
            if dummy.val != -1:
                new_node.next = dummy
            dummy = new_node

        return dummy
