# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/12 21:41

class CQueue:

    def __init__(self):
        self.queue = []

    def appendTail(self, value: int) -> None:
        self.queue.append(value)

    def deleteHead(self) -> int:
        if self.queue:
            return self.queue.pop(0)
        return -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()