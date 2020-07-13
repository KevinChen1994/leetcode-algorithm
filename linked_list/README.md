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
solution1: 先将head的下一个节点存储起来，然后进行翻转，将翻转好的连接链接到new_head后，之后head指针右移进行翻转下一个。
solution2: 递归。
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

    def reverseList(self, head):
        if not head or not head.next:
            return head
        # reverse返回的是已经反转好的链表，使用last进行接收
        last = self.reverseList(head.next)
        # 将head节点进行翻转
        head.next.next = head
        head.next = None
        return last
```

### reserve-linked-list-first-n

> 反转链表前n个节点

```Python
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
```

### reverse-linked-list-ii

[reverse-linked-list-ii](https://leetcode-cn.com/problems/reverse-linked-list-ii/)

> 反转从位置 *m* 到 *n* 的链表。请使用一趟扫描完成反转。

```Python
'''
solution1: 递归进行求解，每次都将m和n进行减一，当m等于1时，相当于反转前n个节点。
solution2: 使用哑结点指向链表，pre指向要反转的子链表的头一个节点，之后进行移动n-m次，进行反转。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverseFirstN(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

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

    def reverseBetween(self, head, m, n):
        dummy_node = ListNode(-1)
        # 哑节点指向链表的头部
        dummy_node.next = head
        pre = dummy_node
        # pre指向要反转的子链表之前一个节点
        for i in range(1, m):
            pre = pre.next
        # head指向的是要反转的子链表的头部
        head = pre.next
        for i in range(m, n):
            # 保存head的下一个节点
            next = head.next
            # head指向下一个节点的下一个节点，也就是向后移动一位
            head.next = next.next
            # next节点移动到需要反转的子链表头部
            next.next = pre.next
            # pre一直为需要反转的子链表的前驱结点
            pre.next = next
        return dummy_node.next
```

### merge-two-sorted-lists

[merge-two-sorted-lists](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

> 将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

```Python
'''
solution1: 遍历合并
solution2: 递归，很慢
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        result = dummy
        while l1 and l2:
            if l1.val > l2.val:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
            else:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
        dummy.next = l1 if l1 else l2
        return result.next

    def mergeTwoLists_2(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        # l2比l1要小，所以将l1放到l2后边
        elif l1.val > l2.val:
            l2.next = self.mergeTwoLists_2(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists_2(l1.next, l2)
            return l1
```

### partition-list

[partition-list](https://leetcode-cn.com/problems/partition-list/)

>给定一个链表和一个特定值 *x*，对链表进行分隔，使得所有小于 *x* 的节点都在大于或等于 *x* 的节点之前。
>
>你应当保留两个分区中每个节点的初始相对位置。

```python
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before_head = ListNode(-1)
        before = before_head
        after_head = ListNode(-1)
        after = after_head
        while head:
            if head.val < x:
                before_head.next = head
                before_head = before_head.next
            else:
                after_head.next = head
                after_head = after_head.next
            head = head.next
        after_head.next = None
        before_head.next = after.next
        return before.next
```

### sort-list

[sort-list](https://leetcode-cn.com/problems/sort-list/)

> 在 *O*(*n* log *n*) 时间复杂度和常数级空间复杂度下，对链表进行排序。

```Python
'''
solution: 利用归并排序。
另外还有一种先将链表中的数字取出来，放到list中，使用list.sort()进行排序，之后在创建一个链表。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        # 使用快慢指针找到链表中间位置
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        right_head = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(right_head)
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(-1)
        result = dummy
        while left is not None and right is not None:
            if left.val < right.val:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next
            dummy = dummy.next
        dummy.next = right if right is not None else left
        return result.next
```

### reorder-list

[reorder-list](https://leetcode-cn.com/problems/reorder-list/)

> 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
> 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
>
> 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

```python
'''
solution: 先利用快慢指针找到链表中间位置，之后将链表后半部分进行翻转，最后合并两个链表。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        right = self.reverse(slow.next)
        # 将左半部分链表切断
        slow.next = None
        self.merge(head, right)

    def reverse(self, head):
        if head is None:
            return head
        dummy = ListNode(-1)
        while head:
            next = head.next
            head.next = dummy.next
            dummy.next = head
            head = next
        return dummy.next

    def merge(self, left, right):
        head = left
        while left and right:
            temp = right.next
            right.next = left.next
            left.next = right
            right = temp
            left = left.next.next
        if right:
            left.next = right
        left = head
```

### linked-list-cycle

[linked-list-cycle](https://leetcode-cn.com/problems/linked-list-cycle/)

> 给定一个链表，判断链表中是否有环。
>
> 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
>

```Python
'''
solution: 通过快慢指针判断，如果是环，快慢指针终会重合，否则不包含环。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

### linked-list-cycle-ii

[linked-list-cycle-ii](https://leetcode-cn.com/problems/linked-list-cycle-ii/)

> 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
>
> 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
>
> 说明：不允许修改给定的链表。
>

```Python
'''
solution: 利用快慢指针，当快慢指针第一次重合时，慢指针回到第一个节点，快指针往后移动一个位置，之后快慢指针用同样的速度前进，再次相遇的节点就是环的入口。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None and head.next is None:
            return None
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            if slow == fast:
                slow = head
                fast = fast.next
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
            else:
                slow = slow.next
                fast = fast.next.next
        return None
```

注意：快慢指针有两种方式：fast = head.next 或者fast = head；**一般用fast = head.next**比较多，因为这样可以知道中点的上一个节点，可以用来删除等操作。

- fast如果初始化为head.next，那么中点在slow.next
- fast如果初始化为head，那么中点在slow

### palindrome-linked-list

[palindrome-linked-list](https://leetcode-cn.com/problems/palindrome-linked-list/)

```Python
'''
solution: 先通过快慢指针将链表分割成两部分，将第二部分进行反转。反转之后与第一部分进行对比。
注意：如果链表长度为奇数，那么第二部分会比第一部分少一个节点；如果链表长度为偶数，那么两部分的长度相同。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        right = self.reverse(slow.next)
        slow.next = None
        left = head
        while right:
            if left.val == right.val:
                left = left.next
                right = right.next
            else:
                return False
        return True

    def reverse(self, head):
        if head is None:
            return head
        dummy = ListNode(-1)
        while head:
            next = head.next
            head.next = dummy.next
            dummy.next = head
            head = next
        return dummy.next
```

### copy-list-with-random-pointer

[copy-list-with-random-pointer](https://leetcode-cn.com/problems/copy-list-with-random-pointer/)

