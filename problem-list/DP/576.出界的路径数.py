
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        count = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # dp矩阵是的定义为在move步下，球的出发点在i,j点时，球在网格内的路径和
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        # 这里定义为1是说在移动为0步，且在起始位置是路径1
        dp[0][startRow][startColumn] = 1
        for move in range(maxMove):
            for i in range(m):
                for j in range(n):
                    # 如果这里不大于1的话，说明经过move步后不能到达i,j这个点，那后边的计算就没有意义了，这样可以节省计算
                    if dp[move][i][j] > 0:
                        for direction in directions:
                            x, y = i + direction[0], j + direction[1]
                            if 0 <= x < m and 0 <= y < n:
                                dp[move + 1][x][y] = (dp[move + 1][x][y] + dp[move][i][j]) % MOD
                            else:
                                count = (count + dp[move][i][j]) % MOD
        return count
    
if __name__ == '__main__':
    solution = Solution()
    # res = solution.findPaths(2, 2, 2, 0, 0)
    res = solution.findPaths(2, 2, 0, 0, 0)
    print(res)