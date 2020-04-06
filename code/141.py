# !usr/bin/env python
# -*- coding:utf-8 _*-
# datatime:2020/4/5 23:46
'''
solution1: 暴力法。设定一个visited的列表，每次访问节点之前都去查看visited中是否存在当前节点，如果存在说明存在环，
如果不存在就将节点存放到visited中。时间复杂度O(n)，空间复杂度O(n)
solution2: 快慢指针。慢指针每次移动一个距离，快指针每次移动两个距离，如果快慢指针相遇了，说明存在环，如果快指针先为空了，说明不存在环。
时间复杂度O(n)，空间复杂度O(1)
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle_1(self, head):
        visited = []
        while head:
            if head in visited:
                return True
            else:
                visited.append(head)
                head = head.next
        return False

    def hasCycle(self, head):
        '''这串代码的细节实在是太多了，正如链表一般，链表要考虑next，还有开头的特殊情况。'''
        if not head or not head.next: return False  # 去除杂数据
        slow, fast = head, head.next  # 这边要写head.next，不然会报错
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
