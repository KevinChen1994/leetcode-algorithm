# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/27 23:32

'''
solution1: 先统计链表长度，然后在遍历就好
solution2: 定义与head相同的两个链表，一个链表先遍历k个结点，另外一个节点开始进行遍历，当前一个链表遍历结束，第二个链表正好遍历到倒数第二个。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        list_len = 0
        node = head
        while node:
            list_len += 1
            node = node.next
        for i in range(list_len - k):
            head = head.next
        return head

    def getKthFromEnd(self, head, k):
        former, later = head, head
        for i in range(k):
            former = former.next
        while former:
            later, former = later.next, former.next
        return later