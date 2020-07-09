# 链表

## 基本技能

链表相关的核心点

- null/nil 异常处理
- dummy node 哑结点
- 快慢指针
- 插入一个节点到排序链表
- 从一个链表中删除一个节点
- 翻转链表
- 合并两个链表
- 找到了链表的中间节点

## 常见题型

### remove-duplicates-from-sorted-list

[remove-duplicates-from-sorted-list](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/)

> 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

```python
'''
solution1: 非递归，速度快
solution2: 递归
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    def deleteuplicates(self, head):
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head
```

### remove-duplicates-from-sorted-list-ii

[remove-duplicates-from-sorted-list-ii](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/)

> 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 *没有重复出现* 的数字。

```python
'''
solution: 由于第一个结点可能会被删除，所以需要使用dummy node作为辅助。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy_node = ListNode(-1)
        dummy_node.next = head
        a = dummy_node
        b = head.next
        while b is not None:
            if a.next.val != b.val:
                a = a.next
                b = b.next
            else:
                # 这里要先判断b是不是None，否则会报错
                while b is not None and a.next.val == b.val:
                    b = b.next
                # 把去重过的b接到a后边，b往后走一个节点，如果b是最后一个节点那么就是None，否则是下一个节点。
                a.next = b
                b = None if b is None else b.next
        return dummy_node.next
```

### reverse-linked-list

> 反转一个单链表。

```python
'''
solution: 先将head的下一个节点存储起来，然后进行翻转，将翻转好的连接链接到new_head后，之后head指针右移进行翻转下一个。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = ListNode(-1)
        while head is not None:
            # 用来保存下一个节点
            next = head.next
            # 进行翻转
            head.next = new_head.next
            # 将new_head指向翻转的链表
            new_head.next = head
            # 指针右移
            head = next
        return new_head.next
```

