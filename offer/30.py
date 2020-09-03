# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/3 22:37
'''
参考155
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_num = float('inf')

    def push(self, x: int) -> None:
        if x <= self.min_num:
            self.stack.append(self.min_num)
            self.min_num = x
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) != 0:
            if self.min_num == self.stack.pop():
                self.min_num = self.stack.pop()
        else:
            return None

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None

    def min(self) -> int:
        if self.min_num != float('inf'):
            return self.min_num
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
