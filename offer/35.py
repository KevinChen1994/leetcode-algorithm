# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/9 17:39
'''
solution1: python 支持深度拷贝，直接调用库函数即可。
solution2: 使用dfs，从头结点开始拷贝，每次创建一个拷贝节点，依次使用dfs进行拷贝下一个节点和随机节点。
solution3: 使用bfs，使用队列存储没有拷贝的结点，依次去拷贝当前节点的下一个节点和随机节点，并把创建的新节点放到队列中去。（代码有点不太好理解）
solution4: 按顺序进行拷贝，先拷贝当前这个节点，然后通过getCopiedNode方法去拷贝下一个节点和随机节点，如果不存在节点就去创建一个。
solution5: 对solution4的优化
'''


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node):
        import copy
        return copy.deepcopy(head)

    def copyRandomList(self, head: Node) -> Node:
        def dfs(node):
            if not node:
                return
            if node in visited:
                return visited[node]
            copy = Node(node.val, None, None)
            visited[node] = copy
            copy.next = dfs(node.next)
            copy.random = dfs(node.random)
            return copy

        visited = {}
        return dfs(head)

    def copyRandomList(self, head: Node):
        visited = {}

        def bfs(node):
            if not node:
                return
            copy = Node(node.val, None, None)
            visited[node] = copy
            queue = []
            queue.append(node)
            while queue:
                tmp = queue.pop(0)
                if tmp.next and tmp.next not in visited:
                    visited[tmp.next] = Node(tmp.next.val, None, None)
                    queue.append(tmp.next)
                if tmp.random and tmp.random not in visited:
                    visited[tmp.random] = Node(tmp.random.val, None, None)
                    queue.append(tmp.random)
                # 字典使用get方法如果key是空的话，不会报错，会返回None值
                visited[tmp].next = visited.get(tmp.next)
                visited[tmp].random = visited.get(tmp.random)
            return copy

        return bfs(head)

    def copyRandomList(self, head: Node):
        visited = {}

        def getCopiedNode(node):
            if node:
                if node in visited:
                    return visited[node]
                else:
                    visited[node] = Node(node.val, None, None)
                    return visited[node]
            return None

        if not head:
            return head
        old_node = head
        new_node = Node(old_node.val, None, None)
        visited[old_node] = new_node

        while old_node:
            new_node.next = getCopiedNode(old_node.next)
            new_node.random = getCopiedNode(old_node.random)

            old_node = old_node.next
            new_node = new_node.next
        return visited[head]

    def copyRandomList(self, head: Node):
        if not head:
            return head
        cur = head
        while cur:
            new_node = Node(cur.val, None, None)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        cur_old_list = head
        cur_new_list = head.next
        new_head = head.next
        while cur_old_list:
            cur_old_list.next = cur_old_list.next.next
            cur_new_list.next = cur_new_list.next.next if cur_new_list.next else None
            cur_old_list = cur_old_list.next
            cur_new_list = cur_new_list.next
        return new_head



