# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/6 15:55
from typing import List
'''
solution1: 暴力法。这道题的问题就是找到当前柱子左右两边最高的柱子，根据木桶效应，当前柱子能装的水取决于两边最短的柱子。
solution2: 动态规划，依次求出每个位置左右两边最高的柱子，然后在进行判断。
solution3: 双指针，两个指针分别在数组的前后，使用两个变量存储当前左边最大和右边最大的值，判断哪个小就在那边进行计算。
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0
        for i in range(1, n - 1):
            max_left = max(height[0:i])
            max_right = max(height[i + 1:n])
            result += max(min(max_left, max_right) - height[i], 0)

        return result

    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0
        max_left = [0 for _ in range(n)]
        max_right = [0 for _ in range(n)]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i - 1])
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])
        for i in range(1, n - 1):
            result += max(min(max_left[i], max_right[i]) - height[i], 0)
        return result

    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        result = 0
        left = 0
        right = n - 1
        max_left = height[left]
        max_right = height[right]
        while left < right:
            if max_left < max_right:
                result += max(max_left - height[left], 0)
                left += 1
                max_left = max(max_left, height[left])
            else:
                result += max(max_right - height[right], 0)
                right -= 1
                max_right = max(max_right, height[right])
        return result


if __name__ == '__main__':
    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(solution.trap(height))
