# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/13 23:42

'''
solution: 在原链表的每个结点旁边增加一个拷贝节点，将拷贝的结点正确赋值后连接成一个新的链表。
'''
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        ptr = head
        # 在原链表的没个节点旁边增加一个节点
        while ptr:
            new_code = Node(ptr.val, None, None)
            new_code.next = ptr.next
            ptr.next = new_code
            ptr = new_code.next
        ptr = head
        # 将复制链表的random指向对应的位置
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
        # 将赋值链表的next指向对应的位置
        ptr_old_list = head
        ptr_new_list = head.next
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_old
