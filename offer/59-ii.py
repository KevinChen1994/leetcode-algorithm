# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/15 23:20
'''
solution: 使用一个辅助队列，在由数据入队的时候，判断当前要入队的数字是否大于辅助队列最后一个数字，如果大于，那么将队列最后一个数字弹出，直至遇到大于当前这个数字的数。
这样就保证了辅助队列中存储的是由大到小排列的，在队列弹出的时候，只需要判断弹出的数字是否为辅助队列中的第一个数字即可，如果是那么将辅助队列中的第一个数字弹出，这时，
辅助队列中第二大的数字变成队列的最大的数字，保证了一直记录了当前最大的数字。
'''
class MaxQueue:

    def __init__(self):
        self.queue = []
        self.assitance = []

    def max_value(self) -> int:
        if len(self.assitance) > 0:
            return self.assitance[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        while self.assitance and value > self.assitance[-1]:
            self.assitance.pop()
        self.queue.append(value)
        self.assitance.append(value)

    def pop_front(self) -> int:
        if len(self.queue) > 0:
            res = self.queue.pop(0)
            if res == self.assitance[0]:
                self.assitance.pop(0)
            return res
        else:
            return -1

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

# ["MaxQueue","pop_front","pop_front","pop_front","pop_front","pop_front","push_back","max_value","push_back","max_value"]
# [[],[],[],[],[],[],[15],[],[9],[]]

obj = MaxQueue()
obj.pop_front()
obj.pop_front()
obj.pop_front()
obj.pop_front()
obj.pop_front()
obj.push_back(15)
obj.max_value()
obj.push_back(9)
obj.max_value()


