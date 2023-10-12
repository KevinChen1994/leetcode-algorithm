# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/6 13:45
from typing import List

'''
solution1: 确定好上下左右四个边界，如果到达任意个边界，就进行下一个方向的遍历。
solution2: 我最初的想法是这样，对于这种遍历矩阵的我喜欢用四个方向进行遍历，将访问过的元素设置为v，
依次更新一个位置，直到所有的位置都是v。
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        up = 0
        down = m - 1
        left = 0
        right = n - 1
        result = []
        while True:
            for i in range(left, right + 1):
                result.append(matrix[up][i])
            up += 1
            if up > down: break
            for i in range(up, down + 1):
                result.append(matrix[i][right])
            right -= 1
            if right < left: break
            for i in range(right, left - 1, -1):
                result.append(matrix[down][i])
            down -= 1
            if down < up: break
            for i in range(down, up - 1, -1):
                result.append(matrix[i][left])
            left += 1
            if left > right: break

        return result

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        i, j = 0, 0
        flag = 0
        for _ in range(m * n):
            result.append(matrix[i][j])
            matrix[i][j] = 'v'
            i_tmp = i + directions[flag][0]
            j_tmp = j + directions[flag][1]
            if 0 <= i_tmp < m and 0 <= j_tmp < n and matrix[i_tmp][j_tmp] != 'v':
                i, j = i_tmp, j_tmp
            else:
                flag = (flag + 1) % len(directions)
                i += directions[flag][0]
                j += directions[flag][1]
        return result


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(solution.spiralOrder(matrix))
