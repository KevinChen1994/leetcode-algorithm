# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/12/29 13:58
from typing import List
'''
solution: 定义up和down两个列表，初始化为1，用来存储以i为结尾，最长的turbulent数组。
如果当前值大于上一个值，那么这呈现的是上升的趋势，所以来计算up，up的计算方式为，下降数组down在上一个元素的值加1.
同理，如果当前值小于上一个值，那么呈现的是下降的确实，计算down的方式为，上升数组up在上一个元素的值加1.
这样，如果是连续的turbulent数组，那么up和down会接替进行计算，值也就会累加。如果其中某个元素断了，那么计算需要从1开始。
'''

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up = [1 for _ in range(len(arr))]
        down = [1 for _ in range(len(arr))]
        ans = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                up[i] = down[i-1] + 1
            if arr[i] < arr[i-1]:
                down[i] = up[i-1] + 1
            ans = max(ans, up[i], down[i])
        return ans


if __name__ == '__main__':
    solution = Solution()
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    # (A[1] > A[2] < A[3] > A[4] < A[5])
    print(solution.maxTurbulenceSize(arr))
