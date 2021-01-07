# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/7 10:55
'''
solution: 这种链表reverse的题套路都很接近，看他们需要怎么reverse，有整个reverse的，有reverse前n个的，
这道题是交替reverse，那做法也差不多。
首先将head.next保存起来为next，然后将head.next指向next.next，也就是指向head的下一个的下一个；
然后将next.next指向head，也就是往回指；
然后将pre指向next，这时已经将前两个节点替换位置了，并且pre指向的是替换顺序的链表。
前边是基本操作，后边就是为了这道题做的改变：
移动pre，使pre在head的位置，并且head往后移动一个位置，这样在下次基本操作的时候交换的就是Pre后边的两个节点了，也就是3和4的位置。

针对啥时候dummy.next会变化一直搞不太明白，基本原理是这样的：
dummy跟pre指向的是同一个地址，如果pre.next变了，那dummy.next也变了；
如果只是为pre赋值，这时的pre跟之前的pre不一样了，所以这时候即使改变pre.next，也并不会影响到dummy.next。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while head and head.next:
            next = head.next
            head.next = next.next
            next.next = head
            pre.next = next

            pre = head
            head = head.next
        return dummy.next