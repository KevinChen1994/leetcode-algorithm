# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/13 23:18
'''
solution: 先通过快慢指针将链表分割成两部分，将第二部分进行反转。反转之后与第一部分进行对比。
注意：如果链表长度为奇数，那么第二部分会比第一部分少一个节点；如果链表长度为偶数，那么两部分的长度相同。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        right = self.reverse(slow.next)
        slow.next = None
        left = head
        while right:
            if left.val == right.val:
                left = left.next
                right = right.next
            else:
                return False
        return True

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
