# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/1/16 15:46
# software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 遍历两遍
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


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeNthFromEnd([1, 2, 3, 4, 5], 2))
