# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/22 17:18
from typing import List
'''
solution: 这道题与85最大矩形看似类似，实际解法有很大区别。因为矩阵的长款不同，所以长宽都需要求出来，而正方形长宽相等，
只需要求出一个即可。求边长的方法可以通过动态规划求解，用dp[i][j]代表当前位置最大的边长，这个边长与其左、左上、上的最大边长有关，
如果当前位置的左、左上、上都是正方形，那么当前位置的边长是以这三个位置的最短的那个边长决定的，画图比较好理解，
https://leetcode-cn.com/problems/maximal-square/solution/li-jie-san-zhe-qu-zui-xiao-1-by-lzhlyle/这里有图。
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        width = 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    width = max(width, dp[i][j])
        return width ** 2


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(solution.maximalSquare(matrix))
