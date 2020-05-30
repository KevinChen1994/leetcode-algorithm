# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/2 22:43
'''
solution: DFS+先序优先遍历
'''

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

        def ser(root, array):
            if not root:
                array.append('None')
            else:
                array.append(root.val)
                ser(root.left, array)
                ser(root.right, array)
            return array

        return ser(root, [])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def des(data_):
            if data_[0] == 'None':
                data_.pop(0)
                return None
            root = TreeNode(data_[0])
            data_.pop(0)
            root.left = des(data)
            root.right = des(data)

            return root

        root = des(data)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
