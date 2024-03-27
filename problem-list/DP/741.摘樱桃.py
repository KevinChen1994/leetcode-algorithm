from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[float('-inf')] * (n + 1) for _ in range(n + 1)]for _ in range(2 * n + 1)]

        dp[2][1][1] = grid[0][0]
        for k in range(3, 2 * n + 1):
            for i1 in range(n + 1):
                for i2 in range(n + 1):
                    j1, j2 = k - i1, k-i2
                    if (j1 <= 0 or j1 > n or j2 <= 0 or j2 > n):
                        continue
                    A, B = grid[i1 -1][j1 - 1], grid[i2 - 1][j2 - 1]
                    if (A == -1 or B == -1):
                        continue
                    a, b, c, d = dp[k - 1][i1 -1][i2], dp[k - 1][i1 -1][i2 - 1], dp[k - 1][i1][i2 - 1], dp[k - 1][i1][i2]
                    t = max(max(a, b), max(c, d)) + A
                    if (i1 != i2):
                        t += B
                    dp[k][i1][i2] = t
        
        return 0 if dp[2*n][n][n] <= 0 else dp[2*n][n][n]


if __name__ == '__main__':
    solution = Solution()
    grid = [
            [0,1,-1],
            [1,0,-1],
            [1,1,1]
            ]
    grid = [
        [1,1,-1],
        [1,-1,1],
        [-1,1,1]
        ]
    res = solution.cherryPickup(grid)
    print(res)