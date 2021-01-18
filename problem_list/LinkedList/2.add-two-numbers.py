# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/8 15:31

# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        pre = dummy
        ten = 0
        while l1 and l2:
            new_value = l1.val + l2.val + ten
            if new_value >= 10:
                new_value -= 10
                ten = 1
            else:
                ten = 0
            new_node = ListNode(new_value)
            pre.next = new_node
            pre = new_node
            l1 = l1.next
            l2 = l2.next
            if not l1:
                while l2:
                    new_value = l2.val + ten
                    if new_value >= 10:
                        new_value -= 10
                        ten = 1
                    else:
                        ten = 0
                    new_node = ListNode(new_value)
                    pre.next = new_node
                    pre = new_node
                    l2 = l2.next
                if ten:
                    new_node = ListNode(ten)
                    pre.next = new_node
                    ten = 0
            if not l2:
                while l1:
                    new_value = l1.val + ten
                    if new_value >= 10:
                        new_value -= 10
                        ten = 1
                    else:
                        ten = 0
                    new_node = ListNode(new_value)
                    pre.next = new_node
                    pre = new_node
                    l1 = l1.next
                if ten:
                    new_node = ListNode(ten)
                    pre.next = new_node
                    ten = 0
        if ten:
            new_node = ListNode(ten)
            pre.next = new_node
        return dummy.next

    # 更为简洁的一种方法
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        ten = 0
        dummy = ListNode(-1)
        pre = dummy
        while l1 or l2:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            sum = l1_value + l2_value + ten
            ten = sum // 10
            new_node = ListNode(sum % 10)
            pre.next = new_node
            pre = new_node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if ten:
            new_node = ListNode(ten)
            pre.next = new_node
        return dummy.next

