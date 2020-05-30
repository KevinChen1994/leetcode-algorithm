# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/2/25 14:43
# software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 暴力法，先将所有链表的数据放到list中，通过快排排序，之后写到一个链表中。
    def mergeKLists_1(self, lists):
        all_data = []
        for l in lists:
            while l:
                all_data.append(l.val)
                l = l.next
        self.quick_sort(all_data, 0, len(all_data) - 1)
        head = ListNode(0)
        all_node = head
        for i in all_data:
            node = ListNode(i)
            all_node.next = node
            all_node = all_node.next
        return head.next

    def quick_sort(self, li, start, end):
        # 分治 一分为二
        # start=end ,证明要处理的数据只有一个
        # start>end ,证明右边没有数据
        if start >= end:
            return
        # 定义两个游标，分别指向0和末尾位置
        left = start
        right = end
        # 把0位置的数据，认为是中间值
        mid = li[left]
        while left < right:
            # 让右边游标往左移动，目的是找到小于mid的值，放到left游标位置
            while left < right and li[right] >= mid:
                right -= 1
            li[left] = li[right]
            # 让左边游标往右移动，目的是找到大于mid的值，放到right游标位置
            while left < right and li[left] < mid:
                left += 1
            li[right] = li[left]
        # while结束后，把mid放到中间位置，left=right
        li[left] = mid
        # 递归处理左边的数据
        self.quick_sort(li, start, left - 1)
        # 递归处理右边的数据
        self.quick_sort(li, left + 1, end)

    # 分而治之，链表两两合并
    def mergeKLists_2(self, lists):
        if not lists: return
        n = len(lists)
        return self.merge(lists, 0, n - 1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    solution = Solution()
    array = [2, 3, 5, 7, 1, 4, 6, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
    solution.quick_sort(array, 0, len(array) - 1)
    print(array)
