# -*- coding:utf-8 -*-
# author: chenmeng
# datetime:2023/1/29 10:30
# Description:

'''
solution: 需要确定好如何才能构成一个正方形，那就是当前是1，四条边也都是1，并且长度相等。
按照这个规则，首先解决当前是1，当前是1的话，可以通过dp矩阵记录下来当前的长度，当前的长度取决于左边和上边1的个数，需要用两个dp矩阵记录；
使用一个dp矩阵记录左边是1的个数，使用一个dp矩阵记录上边1的个数；
那正方形的边长就是当前位置下，两个矩阵的最小值，记录为k。
四个边都是1的判断方法，首先明确正方形的边长k，就已经确定下边和右边都为1了；
那左边都是1，需要根据记录当前位置下上方连续是1的dp矩阵来判断，用当前位置减去k长度的位置，其长度是否大于等于k，也就是左下角的点上部有几个1；
上边都是1的判断方法同理，根据记录当前位置下左边连续是1的dp矩阵判断，用当前位置减去k长度的位置，其长度是否大于等于k，也就是右上角的点左部有几个1；
此时k是最小边长，面积为k的平方。
'''

from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # l表示点i,j左侧连续1的个数，u表示i,j上方连续1的个数
        l = [[0 for _ in range(n)] for _ in range(m)]
        u = [[0 for _ in range(n)] for _ in range(m)]

        max_len = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                l[i][j], u[i][j] = 1, 1
                if i > 0:
                    u[i][j] += u[i - 1][j]
                if j > 0:
                    l[i][j] += l[i][j - 1]
                # 以当前的1为右下角要构成正方形, 其边长最长只可能是左边最长连续的1与上面最长连续的1的个数取最小值
                for k in range(min(u[i][j], l[i][j]), 0, -1):
                    # 判断第i行的第j - k列的上面1的个数, 和第i - k行的第j列的左边的1的个数是否都大于等于k，都大于等于k说明能够构成正方形
                    if k > max_len and u[i][j - k + 1] >= k and l[i - k + 1][j] >= k:
                        max_len = k
        return max_len ** 2


if __name__ == '__main__':
    solution = Solution()
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    # grid = [[1,1,0,0]]
    solution.largest1BorderedSquare(grid)
