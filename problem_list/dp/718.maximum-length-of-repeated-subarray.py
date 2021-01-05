# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/5 16:32
from typing import List

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        l1 = len(A)
        l2 = len(B)
        ans = 0
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(ans, dp[i][j])

        return ans

if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    print(solution.findLength(A, B))