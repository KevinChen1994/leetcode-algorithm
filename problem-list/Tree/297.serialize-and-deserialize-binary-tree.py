# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/4 23:23

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

        def dfs(root, array):
            if not root:
                array.append('None')
            else:
                array.append(root.val)
                dfs(root.left, array)
                dfs(root.right, array)
            return array

        return dfs(root, [])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs(data):
            if data[0] == 'None':
                data.pop(0)
                return None
            root = TreeNode(data[0])
            data.pop(0)
            root.left = dfs(data)
            root.right = dfs(data)
            return root

        return dfs(data)
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
