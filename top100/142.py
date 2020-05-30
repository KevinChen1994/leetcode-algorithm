# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/6 20:58
'''
solution1: 暴力法。
solution2: 数学公式计算。详见https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle_1(self, head):
        visited = []
        while head:
            if head in visited:
                return head
            else:
                visited.append(head)
                head = head.next
        return None

    def detectCycle_2(self, head):
        slow, fast = head, head
        while True:
            if not (fast and fast.next): return
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        fast = head
        while fast != slow:
            slow, fast = slow.next, fast.next
        return fast
