# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/3/1 14:26
'''
solution: 使用二维dp矩阵记录状态，dp[i][0]代表当前位置不进行交换的最少交换次数，dp[i][1]代表当前位置交换的最少交换次数。
如果当前位置A[i]>A[i-1] and B[i] > B[i - 1]，那么这是交换不交换都可以，不交换的话，dp[i][0] = dp[i-1][0]，也就是上一个位置也不交换；
交换的话，需要将i-1位置也进行交换，也就是dp[i][1] = dp[i - 1][1] + 1，上一个位置进行交换，当前也交换，所以需要加1。
如果当前位置B[i] > A[i - 1] and A[i] > B[i - 1]，也就是十字交叉对比，这时有两种情况：
如果当前位置不交换的话：当前位置不交换，上一个位置交换dp[i - 1][1]；
如果当前位置交换的话：上一个位置不交换，当前位置交换；
'''
from typing import List


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        dp = [[float('inf'), float('inf')] for _ in range(n)]
        dp[0][0], dp[0][1] = 0, 1
        for i in range(1, n):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1] + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                dp[i][0] = min(dp[i][0], dp[i-1][1])
                dp[i][1] = min(dp[i][1], dp[i-1][0] + 1)
        return min(dp[-1])


if __name__ == '__main__':
    solution = Solution()
    A = [1, 3, 5, 4]
    B = [1, 2, 3, 7]
    print(solution.minSwap(A, B))
