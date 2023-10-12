# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/22 17:46
from typing import List

'''
solution: 利用dp求出每个位置为右下角，(0,0)为左上角的面积，面积=当前位置上方元素的面积+当前位置左侧元素的面积+当前位置的大小-重叠部分面积。
'''


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        self.dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.dp[i + 1][j + 1] = self.dp[i + 1][j] + self.dp[i][j + 1] + matrix[i][j] - self.dp[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    print(obj.sumRegion(2, 1, 4, 3))
