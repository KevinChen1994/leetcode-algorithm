# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/22 23:10
'''
solution1: 动态插入元素，使元素保证从小到大排序。
solution2: 使用堆，实现两个堆，一个小顶堆，存储较大的一半元素，一个大顶堆，存储较小的一半元素。
求中位数时，奇数的话，就取小顶堆的堆定，偶数的话，就取小顶堆和大顶堆堆定的平均。
solution3: 对solution2的优化。
'''
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        if len(self.nums) > 0:
            if num <= self.nums[0]:
                self.nums.insert(0, num)
            elif num >= self.nums[len(self.nums) - 1]:
                self.nums.append(num)
            else:
                for i in range(len(self.nums)):
                    if num <= self.nums[i]:
                        self.nums.insert(i, num)
                        break
                if i == len(self.nums) - 1:
                    self.nums.append(num)
        else:
            self.nums.append(num)

    def findMedian(self) -> float:
        if len(self.nums) != 0 and len(self.nums) % 2 == 0:
            return (self.nums[len(self.nums) // 2 - 1] + self.nums[len(self.nums) // 2]) / 2
        elif len(self.nums) != 0 and len(self.nums) % 2 != 0:
            return self.nums[len(self.nums) // 2]
        else:
            return None


from heapq import *


class MedianFinder:
    def __init__(self):
        self.A = []  # 小顶堆，保存较大的一半
        self.B = []  # 大顶堆，保存较小的一半

    # N为偶数时，向A插入元素，插入方法为先将元素插入B，然后将B栈顶元素弹出并插入A，这样保证了插入A的都是较大的元素。
    # N为奇数时，向B插入元素，插入方法为先将元素插入A，然后将A栈顶元素弹出并插入B，这样保证了插入B的都是较小的元素。
    # heap默认生成的是小顶堆，实现大顶堆的话，将元素取反就行。
    def addNum(self, num):
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self):
        # 这里减法是因为。B是大顶堆，存储的是负数。
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2


class MedianFinder:
    def __init__(self):
        self.A = []
        self.B = []

    def addNum(self, num):
        if len(self.A) != len(self.B):
            heappush(self.B, -heappushpop(self.A, num))
        else:
            heappush(self.A, -heappushpop(self.B, -num))

    def findMedian(self):
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(10)
param_2 = obj.findMedian()
