# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/12 13:26
'''
反转链表前N个节点。
solution: 使用递归，与反转整个链表不同的是，反转整个链表最终需要将head.next=None，因为第一个节点反转后变成最后一个节点；而反转部分链表head节点反转后不一定是最后一个节点，所以需要保存后驱节点successor（第n+1个节点），反转之后将head连接到successor上。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
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

    def stringToListNode(self, numbers):

        # Now convert that list into linked list
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for number in numbers:
            ptr.next = ListNode(number)
            ptr = ptr.next

        ptr = dummyRoot.next
        return ptr

    def listNodeToString(slef, node):
        if not node:
            return "[]"

        result = ""
        while node:
            result += str(node.val) + ", "
            node = node.next
        return "[" + result[:-2] + "]"


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    head = solution.stringToListNode(nums)
    new_head = solution.reverseFirstN(head, 3)
    print(solution.listNodeToString(new_head))
