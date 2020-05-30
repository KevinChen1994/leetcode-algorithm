#-*- coding:utf-8 -*-
# author:chenmeng
# datetime:2019/12/28 20:31
# software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 直接在l1进行修改
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_node, l2_node, carry = l1, l2, 0

        while l1_node or l2_node:
            if l1_node and l2_node:
                val = l1_node.val + l2_node.val + carry
                if val > 9:
                    l1_node.val = val - 10
                    carry = 1
                else:
                    l1_node.val = val
                    carry = 0
                pre = l1_node
                l1_node, l2_node = l1_node.next, l2_node.next

            elif l1_node and not l2_node:
                val = l1_node.val + carry
                if val <= 9:
                    l1_node.val = val
                    carry = 0
                else:
                    l1_node.val = val - 10
                    carry = 1

                pre = l1_node
                l1_node = l1_node.next

            elif not l1_node and l2_node:
                val = l2_node.val + carry
                if val >= 10:
                    new_node = ListNode(0)
                    carry = 1
                    pre.next = new_node
                else:
                    new_node = ListNode(val)
                    carry = 0
                    pre.next = new_node
                pre = new_node
                l2_node = l2_node.next

        if carry == 1:
            newnode = ListNode(1)
            pre.next = newnode

        return l1


# 重新创建一个链表pre，r为指向pre的指针
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = ListNode(0)
        r = pre
        k = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + k
            k = sum // 10
            new_node = ListNode(sum % 10)
            r.next = new_node
            r = r.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if k != 0:
            new_node = ListNode(k)
            r.next = new_node
        return pre.next