# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/9 23:28
'''
solution: 先将head的下一个节点存储起来，然后进行翻转，将翻转好的连接链接到new_head后，之后head指针右移进行翻转下一个。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = ListNode(-1)
        while head is not None:
            # 用来保存下一个节点
            next = head.next
            # 进行翻转
            head.next = new_head.next
            # 将new_head指向翻转的链表
            new_head.next = head
            # 指针右移
            head = next
        return new_head.next
