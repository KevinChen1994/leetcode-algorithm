# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/8 17:55
'''
solution1: 递归调用的归并排序。时间复杂度O(l + r)，l, r 分别代表两个链表长度，空间复杂度O(logn)。思路是通过快慢指针在链表索引中间进行分割，递归调用进行，
直至分割成每个链表只有一个链节点，然后进行比较两个链表头结点的大小进行合并。
solution2: 不使用递归的归并排序。可读性较差。参考https://leetcode-cn.com/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
solution3: 同solution2，可读性较高。

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList_1(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head  # termination.
        # 通过快慢指针在链表中间进行分割
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # save and cut.
        # 递归进行分割，直至分割成每一个链表只有一个链节点
        left, right = self.sortList(head), self.sortList(mid)
        # 将左右链表按大小顺序合并
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

    def sortList_2(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        # 统计链表长度
        while h: h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h: h, i = h.next, i - 1
                if i: break  # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h: h, i = h.next, i - 1
                c1, c2 = intv, intv - i  # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2
        return res.next

    def sortList_3(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head

        current, length = head, 0
        while current:  # 求得链表长度
            current, length = current.next, length + 1

        root = ListNode(0)
        root.next = head
        intv = 1  # 每次合并的规模

        # 根据不同的链表切片规模，每一次都从头进行归并
        while intv < length:
            merge_point, current = root, root.next

            while current:  # 根据当前的合并规模，将链表内的链表切片两两归并

                # 获取当前需要归并的子链表 h1
                h1, intv_residue_1 = current, intv
                while intv_residue_1 and current:
                    current, intv_residue_1 = current.next, intv_residue_1 - 1
                if intv_residue_1:  # h2 在这种情况下不存在，所以本轮不需要合并
                    break

                    # 获取当前需要归并的子链表 h2
                h2, intv_residue_2 = current, intv
                while intv_residue_2 and current:
                    current, intv_residue_2 = current.next, intv_residue_2 - 1

                len1, len2 = intv, intv - intv_residue_2  # len2 的长度可能比 intv 小

                while len1 and len2:  # 归并排序
                    if h1.val < h2.val:
                        merge_point.next, h1, len1 = h1, h1.next, len1 - 1
                    else:
                        merge_point.next, h2, len2 = h2, h2.next, len2 - 1
                    merge_point = merge_point.next

                if len1:  # 归并排序处理一下没有被归并的剩余值
                    merge_point.next = h1
                else:
                    merge_point.next = h2
                while len1 > 0 or len2 > 0:
                    merge_point, len1, len2 = merge_point.next, len1 - 1, len2 - 1

                merge_point.next = current  # h1 和 h2 的归并只是影响了链表的一部分，这里应该把归并后的链表切片跟原链表h2之后的部分拼起来

            intv *= 2

        return root.next
