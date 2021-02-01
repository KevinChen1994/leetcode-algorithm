# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/29 23:09
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n == 0:
            return
        return self.merge_sort(lists, 0, len(lists) - 1)

    def merge_sort(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l = self.merge_sort(lists, left, mid)
        r = self.merge_sort(lists, mid + 1, right)
        return self.merge(l, r)

    def merge(self, left, right):
        dummy = ListNode(-1)
        pre = dummy
        while left and right:
            if left.val < right.val:
                pre.next = left
                left = left.next
            else:
                pre.next = right
                right = right.next
            pre = pre.next
        pre.next = left if left else right
        return dummy
