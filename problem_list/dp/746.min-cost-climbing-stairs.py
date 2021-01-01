# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/12/31 14:53
from typing import List
'''
solution: 做这道题的时候主要是在考虑如何选择起点，后来想到不用考虑起点问题，将这个问题融合进dp就可以解决。
使用dp[i]记录到达i点最少所需体力，那么到达当前位置需要的最小体力，就是上一个位置的最小体力加上从这里起跳所需体力，
与上两个位置最小体力加上从这里起跳所需最小体力之间最小的那一个。dp这里设置的比cost多一位，也就是需要跳完cost所需的最小体力。
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(solution.minCostClimbingStairs(cost))
