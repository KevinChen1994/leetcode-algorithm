# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/5 22:40
'''
solution: 看到是排好序的数组，那准是二分查找。
'''
class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False
        for i in range(n):
            if matrix[i][0] > target:
                return False
            left = 0
            right = m - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[i][mid] > target:
                    right = mid - 1
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 90
    print(solution.findNumberIn2DArray(matrix, target))
