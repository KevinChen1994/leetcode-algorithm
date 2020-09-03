# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/3 21:35
'''
solution1: 自己想的，按照顺时针的方向(右下左上)定义好四个方向的坐标，然后进行遍历。然而耗时贼长，但是我感觉时间复杂度就是O(mn)啊，搞不懂为什么这么耗时。
solution2: 最佳解法，四个方向进行遍历，很好理解。
solution3: 大神代码，膜拜！
'''
class Solution:
    def spiralOrder_1(self, matrix):
        res = []
        m = len(matrix)
        if m == 0:
            return res
        n = len(matrix[0])
        # 顺时针的方向，右下左上
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d_i = 0
        coordinate = (0, 0)
        looked = [(0, 0)]
        res.append(matrix[coordinate[0]][coordinate[0]])
        while len(res) < m * n:
            coordinate = (coordinate[0] + directions[d_i][0], coordinate[1] + directions[d_i][1])
            if -1 < coordinate[0] < m and -1 < coordinate[1] < n and coordinate not in looked:
                res.append(matrix[coordinate[0]][coordinate[1]])
                looked.append(coordinate)
            else:
                coordinate = (coordinate[0] - directions[d_i][0], coordinate[1] - directions[d_i][1])
                d_i = (d_i + 1) % 4
        return res

    def spiralOrder_2(self, matrix):
        res = []
        if not matrix:
            return res
        low, high, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while True:
            for i in range(left, right + 1):
                res.append(matrix[low][i])
            low += 1
            if low > high:
                break
            for i in range(low, high + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[high][i])
            high -= 1
            if low > high:
                break
            for i in range(high, low - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res

    def spiralOrder_3(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res


if __name__ == '__main__':
    solution = Solution()
    # matrix = [[1, 2, 3],
    #           [4, 5, 6],
    #           [7, 8, 9]]
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    print(solution.spiralOrder_3(matrix))
