# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/13 16:47
'''
solution: 先利用快慢指针找到链表中间位置，之后将链表后半部分进行翻转，最后合并两个链表。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        right = self.reverse(slow.next)
        # 将左半部分链表切断
        slow.next = None
        self.merge(head, right)

    def reverse(self, head):
        if head is None:
            return head
        dummy = ListNode(-1)
        while head:
            next = head.next
            head.next = dummy.next
            dummy.next = head
            head = next
        return dummy.next

    def merge(self, left, right):
        head = left
        while left and right:
            temp = right.next
            right.next = left.next
            left.next = right
            right = temp
            left = left.next.next
        if right:
            left.next = right
        left = head
