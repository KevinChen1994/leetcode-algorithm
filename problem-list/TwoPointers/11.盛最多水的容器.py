# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/6 17:39
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                result = max(result, height[left] * (right - left))
                left += 1
            else:
                result = max(result, height[right] * (right - left))
                right -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(height))
