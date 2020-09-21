# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/18 17:03

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('null')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if str(data) == '[]':
            return
        level = data[1:-1].split(',')
        root = TreeNode(int(level[0]), None, None)
        queue = [root]
        i = 1
        while queue:
            node = queue.pop(0)
            if level[i] != 'null':
                node.left = TreeNode(level[i], None, None)
                queue.append(node.left)
            i += 1
            if level[i] != 'null':
                node.right = TreeNode(level[i], None, None)
                queue.append(node.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
