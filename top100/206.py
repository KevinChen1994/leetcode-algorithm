# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/15 22:37
'''
solution1: 暴力法。
solution2: 双指针法。定义pre和cur两个指针，pre首先指向None，cur指向head。然后在遍历cur的过程中，将cur指向pre，然后cur和pre都往前移动一位
solution3: 递归。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList_1(self, head) -> ListNode:
        data_list = []
        new_head = ListNode()
        temp = new_head
        while head:
            data_list.append(head.val)
            head = head.next
        for i in range(len(data_list) - 1, -1, -1):
            node = ListNode(data_list[i])
            temp.next = node
            temp = temp.next
        return new_head.next

    def reverseList_2(self, head):
        pre = None
        cur = head
        while cur:
            # 先将当前节点的下一个节点存储起来
            temp = cur.next
            # 将当前节点指向pre
            cur.next = pre
            # pre 和 cur都前进一位
            pre = cur
            cur = temp
        return pre

    def reverseList_3(self, head):
        if head == None or head.next == None:
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList_3(head.next)
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        head.next = None
        return cur

