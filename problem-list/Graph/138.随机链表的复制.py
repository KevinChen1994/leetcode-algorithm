# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/28 14:10
'''
solution1: algorithm-pattern 138中实现过了，思路是在原结点后添加一个相同的结点，最后再将添加的结点拿出来链到一起。
solution2: 这种方法实现起来会比较简单，创建一个字典，key是原结点，value是复制的结点，需要遍历两次，
第一次先将原结点的val创建出来，next指针和random指针不赋值，第二遍遍历的时候再将这两个指针赋值。
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
        node_dict = {}
        dummy = head
        while dummy:
            node_dict[dummy] = Node(dummy.val, None, None)
            dummy = dummy.next
        dummy = head
        while dummy:
            if dummy.next:
                node_dict[dummy].next = node_dict[dummy.next]
            if dummy.random:
                node_dict[dummy].random = node_dict[dummy.random]
            dummy = dummy.next
        return node_dict[head]
