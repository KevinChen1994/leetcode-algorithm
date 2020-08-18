# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/12 22:25

class Solution:
    def minArray(self, numbers) -> int:
        left = 0
        right = len(numbers) - 1
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] < numbers[left]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right -= 1
        return numbers[left]


if __name__ == '__main__':
    solution = Solution()
    numbers = [2, 2, 2, 0, 1]
    print(solution.minArray(numbers))
