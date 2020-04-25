# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/23 23:02
'''
solution1: 先将链表存储到一个list中，然后翻转list与原始list进行对比，如果相同说明是回文链表。另外，Python翻转链表是很容易操作的，在Java等其他语言中是没有这样的操作的，
所以可以设置两个指针，一个指向开头，另外一个指向结尾，判断两个指针是否相同，相同的话同时移动，直到两个指针相遇。空间复杂度O(n)
solution2: 将链表从中间截断，然后逆转后半部分链表，遍历判断前半部分链表跟逆转的后半部分链表是否相同。最后再将链表合并。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome_1(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

    def isPalindrome_2(self, head):
        if not head: return True
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position:
            # 这里不要直接对比节点，要对比节点的val
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous
