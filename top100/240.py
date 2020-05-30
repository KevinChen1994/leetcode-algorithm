# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/28 21:08
'''
solution1: 二分查找。固定行或者列，使用二分查找进行查找。
solution2: 从矩阵的左下角开始找。如果当前值比target大，就往上走一步，如果当前值比target小，就往右走一步，直到找到target或者超出矩阵范围结束。
'''
class Solution:

    def binary_search(self, matrix, target, start, vertical):
        low = start
        high = len(matrix[0]) - 1 if vertical else len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            # 搜索一列
            if vertical:
                if matrix[start][mid] < target:
                    low = mid + 1
                elif matrix[start][mid] > target:
                    high = mid - 1
                else:
                    return True
            # 搜索一行
            else:
                if matrix[mid][start] < target:
                    low = mid + 1
                elif matrix[mid][start] > target:
                    high = mid - 1
                else:
                    return True
        return False

    def searchMatrix_1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True
        return False

    def searchMatrix_2(self, matrix, target):
        if not matrix: return False
        i = len(matrix)
        j = len(matrix[0])
        row = i - 1
        col = 0
        while col < j and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
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
    target = 5
    print(solution.searchMatrix_2(matrix, target))
