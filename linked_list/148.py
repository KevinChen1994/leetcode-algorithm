# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/13 16:01
'''
solution: 利用归并排序。
另外还有一种先将链表中的数字取出来，放到list中，使用list.sort()进行排序，之后在创建一个链表。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        # 使用快慢指针找到链表中间位置
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        right_head = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(right_head)
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(-1)
        result = dummy
        while left is not None and right is not None:
            if left.val < right.val:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next
            dummy = dummy.next
        dummy.next = right if right is not None else left
        return result.next
