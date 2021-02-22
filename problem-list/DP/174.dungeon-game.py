# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/22 11:03
from typing import List
'''
solution: 
这道题需要考虑到当前位置最少需要的血量是多少，所以需要从耗血量最少的地方往当前位置走，减去当前位置需要的血量，就是当前所需最少的血量。
需要注意最少血量要大于等于1。
这道题的dp是倒序的，这点很重要，为什么不能像【最小路径和】一样是正序的？因为【最小路径和】是无状态的，
你会发现【最小路径和】倒序dp也是可以的，这道题由于有“加血”的过程，只能依赖后面的值判断需要的血量。
所以这里的dp[i][j]表达的意思是：“从（i，j）出发，到达终点需要最少的血量”。因此，正序的含义为“从起点出发，
到达位置（i，j）所需要的最少血量”；倒序的含义是“从（i，j）出发，到达终点需要最少的血量”。初始血量本来就是要求的，
所以只能倒序dp。
'''

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        if m == 0:
            return 0
        n = len(dungeon[0])
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
        return dp[0][0]


if __name__ == '__main__':
    solution = Solution()
    dungeon = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]
    print(solution.calculateMinimumHP(dungeon))
