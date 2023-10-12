# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/27 17:05
from typing import List

'''
solution: 题目容易与200岛屿数量弄混，区别在于这道题添加了一个间接关系，即使1-4没有相连，如果1-2相连和2-4相连，
那么1-2-4属于同一个省。题目弄清楚就容易了，也是利用dfs。
首先明确一点自己跟自己肯定是相连的，所以对角线肯定会是1。那么就从对角线入手，依次判断每个城市分别与其他城市相连的情况，
利用dfs找到直接相连与间接相连的城市，设置为0。
'''


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        if m == 0:
            return 0
        result = 0
        for i in range(m):
            if isConnected[i][i] == 1:
                result += 1
                self.dfs(isConnected, i, m)

        return result

    def dfs(self, isConnected, i, m):
        for j in range(m):
            if isConnected[i][j] == 1:
                isConnected[i][j] = isConnected[j][i] = 0
                self.dfs(isConnected, j, m)


if __name__ == '__main__':
    solution = Solution()
    isConnected = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    # isConnected = [
    #     [1, 0, 0, 1],
    #     [0, 1, 1, 0],
    #     [0, 1, 1, 1],
    #     [1, 0, 1, 1]]
    print(solution.findCircleNum(isConnected))
