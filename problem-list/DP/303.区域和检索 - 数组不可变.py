# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/5 22:38
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_sum = [0]
        for i in range(len(nums)):
            self.nums_sum.append(self.nums_sum[-1] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.nums_sum[j + 1] - self.nums_sum[i]


if __name__ == '__main__':
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    print(numArray.sumRange(0, 2))  # return 1((-2) + 0 + 3)
    print(numArray.sumRange(2, 5))  # return -1(3 + (-5) + 2 + (-1))
    print(numArray.sumRange(0, 5))  # return -3((-2) + 0 + 3 + (-5) + 2 + (-1))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
