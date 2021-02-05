# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/5 10:53
'''
solution1: 序列化通过后序遍历将树转成字符串，反序列化由后到前进行构建树
solution2: 序列化通过前序遍历将树转成字符串，反序列化由前到到进行构建树

这两个方法思想一样，有一个点是二叉搜索树的性质是中序遍历节点的是由小到大进行排列的，也就是根节点大于左子树所有点节点，小于右子树所有的节点。
所以根据这个特点，可判断如果当前节点是根节点的话，那么去构建左子树的时候，根节点的值就是最大值，任何大于这个值的节点都不能构成其左子树；
同理，构建右子树的时候，根节点的值也就是最小值任何小于这个值的节点都不能构成其右子树。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def post_order(root, array):
            if not root:
                pass
            else:
                post_order(root.left, array)
                post_order(root.right, array)
                array.append(root.val)
            return array

        return ' '.join(map(str, post_order(root, [])))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        def helper(low=float('-inf'), high=float('inf')):
            if not data or data[-1] < low or data[-1] > high:
                return None
            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, high)
            root.left = helper(low, val)
            return root

        data = [int(x) for x in data.split(' ') if x]
        return helper()


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def pre_order(root, array):
            if not root:
                pass
            else:
                array.append(root.val)
                pre_order(root.left, array)
                pre_order(root.right, array)
            return array

        return ' '.join(map(str, pre_order(root, [])))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        def helper(low=float('-inf'), high=float('inf')):
            if not data or data[0] < low or data[0] > high:
                return None
            val = data.pop(0)
            root = TreeNode(val)
            root.left = helper(low, val)
            root.right = helper(val, high)
            return root

        data = [int(x) for x in data.split(' ') if x]
        return helper()


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
deser = Codec()
# tree = ser.serialize(root)
ans = deser.deserialize('1 3 2')
# return ans
