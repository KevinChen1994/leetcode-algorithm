
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        # dp[step][i][j]为从i j出发，走step步后留在棋盘的概率
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        for step in range(k + 1):
            for i in range(n):
                for j in range(n):
                    if step == 0:
                        dp[step][i][j] = 1
                    else:
                        for direction in directions:
                            x, y = i + direction[0], j + direction[1]
                            if 0 <= x < n and 0 <= y < n:
                                dp[step][i][j] += dp[step - 1][x][y] / 8
        return dp[k][row][column]
    
if __name__ == '__main__':
    solution = Solution()
    res = solution.knightProbability(3, 2, 0, 0)
    print(res)
