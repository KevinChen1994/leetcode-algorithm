# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/11 20:53
'''
solution1: 使用栈作为辅助。初始化helper作为辅助栈，与stack长度相同，在对应的位置存储当前最小值。
solution2: 只使用一个栈，维护一个全局最小值，在push的时候做一些调整：如果push的x比当前最小值还要小，现将当前最小值push进栈中，再push x。
原因是如果当前pop出去的值为最小值，那么就会丢失掉第二小的最小值是哪个，这样可以强制存储一遍当前时刻的最小值。
'''

class MinStack_1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.helper) > 0:
            if x < self.helper[-1]:
                self.helper.append(x)
            else:
                self.helper.append(self.helper[-1])
        else:
            self.helper.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.helper.pop()

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.helper[-1]

class MinStack_2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min:
            self.min = self.stack.pop()

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.min


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack_1()
    # obj.push(2)
    # obj.push(1)
    # obj.push(0)
    # param_2 = obj.getMin()
    # print(param_2)
    # param_3 = obj.top()
    # print(param_3)
    # obj.pop()
    # param_4 = obj.getMin()
    # print(param_4)
    # ["MinStack", "push", "push", "push", "top", "pop", "getMin", "pop", "getMin", "pop", "push", "top", "getMin",
    #  "push", "top", "getMin", "pop", "getMin"]
    # [[], [2147483646], [2147483646], [2147483647], [], [], [], [], [], [], [2147483647], [], [], [-2147483648], [], [],
    #  [], []]
    obj.push(2147483646)
    obj.push(2147483646)
    obj.push(2147483647)
    a = obj.top()
    print(a)
    obj.pop()
    b = obj.getMin()
    print(b)
    obj.pop()
    c = obj.getMin()
    print(c)
    obj.pop()
    obj.push(2147483647)
    d = obj.top()
    print(d)
    e = obj.getMin()
    print(e)
    obj.push(-2147483648)
    f = obj.top()
    print(f)
    g = obj.getMin()
    print(g)
    obj.pop()
    h = obj.getMin()
    print(h)
