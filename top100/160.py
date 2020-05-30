# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/12 21:10
'''
solution: 假定链表ab有重合部分，那么链表a的长度为a+c，链表b的长度为b+c，c为链表ab重合部分，因为两个链表重合，所以a+c+b+c = b+c+a+c,
即一个指针A和指针B从两个链表开始遍历，直到其中一个指针为空，然后让该指针指向另外一个链表，继续进行遍历，直到另外一个指针也为空，也让他指向另外一个链表，
如果两个链表有重合部分的话，那么最终这两个指针终会相等。
也可以这么理解，相同的路程，两个人速度也相同，即使起点不同，最终两个人也能同时到达终点，并且最后一段相同的路两个人会一起走。
正所谓错的人永远不会相遇，对的人迟早会相逢！这道题太浪漫了！
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA