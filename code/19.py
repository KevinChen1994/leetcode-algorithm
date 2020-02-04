# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/1/16 15:46
# software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 单指针，遍历两遍
    def removeNthFromEnd_1(self, head, n):
        p = head
        count = 0
        # 计算链表长度
        while p:
            p = p.next
            count += 1
        p = head
        # 确定要删除的结点的索引
        id = count - n
        if id == 0:
            return head.next
        for i in range(count):
            if i == id - 1:
                p.next = p.next.next
            else:
                p = p.next
        return head

    # 双指针，遍历一遍
    def removeNthformEnd_2(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        # 设置双指针
        fast, slow = dummy, dummy
        # 快指针先移动n个结点
        for i in range(n):
            fast = fast.next
        # 同时移动快指针与慢指针，直到快指针指到最后一个结点
        while fast.next:
            slow = slow.next
            fast = fast.next
        # 此时慢指针所指结点为要删除的结点的前一个
        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeNthFromEnd([1, 2, 3, 4, 5], 2))
