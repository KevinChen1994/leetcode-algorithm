# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/18 23:15
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n < 2:
            return
        l = 0
        r = n - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

if __name__ == '__main__':
    solution = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(numbers, target))