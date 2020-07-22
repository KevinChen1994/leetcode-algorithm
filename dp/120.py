# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/21 16:58

# DFS 超时。f(i,j)=min(f(i+1,j),f(i+1,j+1))+triangle[i][j]
class Solution:
    def minimumTotal(self, triangle):
        return self.dfs(0, 0, triangle)

    def dfs(self, level, c, triangle):
        if level == len(triangle):
            return 0
        left = self.dfs(level + 1, c, triangle)
        right = self.dfs(level + 1, c + 1, triangle)
        return min(left, right) + triangle[level][c]


# DFS 带有备忘录，减少运算
class Solution:
    def minimumTotal(self, triangle):
        self.memo = [[0 for i in range(len(triangle))] for j in range(len(triangle))]
        return self.dfs(0, 0, triangle)

    def dfs(self, level, c, triangle):
        if level == len(triangle):
            return 0
        if self.memo[level][c] != 0:
            return self.memo[level][c]
        self.memo[level][c] = min(self.dfs(level + 1, c, triangle), self.dfs(level + 1, c + 1, triangle)) + \
                              triangle[level][c]
        return self.memo[level][c]


# DP dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]
class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]


if __name__ == '__main__':
    solution = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(solution.minimumTotal(triangle))
