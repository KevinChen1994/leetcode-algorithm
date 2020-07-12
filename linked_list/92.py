# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/10 16:38
'''
solution1: 递归进行求解，每次都将m和n进行减一，当m等于1时，相当于反转前n个节点。
solution2: 使用哑结点指向链表，pre指向要反转的子链表的头一个节点，之后进行移动n-m次，进行反转。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverseFirstN(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

    def reverseFirstN(self, head: ListNode, n):
        if n == 1:
            return head
        # 以head.next为起点，反转前n-1个节点
        new_head = self.reverseFirstN(head.next, n - 1)
        # 用来保存第n+1个节点
        successor = head.next.next
        # 反转当前节点
        head.next.next = head
        # 将反转好的结点拼接到后边未反转的结点上
        head.next = successor
        return new_head

    def reverseBetween(self, head, m, n):
        dummy_node = ListNode(-1)
        # 哑节点指向链表的头部
        dummy_node.next = head
        pre = dummy_node
        # pre指向要反转的子链表之前一个节点
        for i in range(1, m):
            pre = pre.next
        # head指向的是要反转的子链表的头部
        head = pre.next
        for i in range(m, n):
            # 保存head的下一个节点
            next = head.next
            # head指向下一个节点的下一个节点，也就是向后移动一位
            head.next = next.next
            # next节点移动到需要反转的子链表头部
            next.next = pre.next
            # pre一直为需要反转的子链表的前驱结点
            pre.next = next
        return dummy_node.next
