# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/11 22:54

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result[::-1]