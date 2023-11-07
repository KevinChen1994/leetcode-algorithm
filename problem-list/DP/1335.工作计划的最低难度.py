from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        # dp[i][j] 代表执行i项工作，前j天的最小难度
        dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for j in range(1, d + 1):
            for i in range(j, n + 1):
                maxDifficulty = 0
                # 这里需要从后往前遍历，因为：1. 当day=1时状态没有进行初始化，所以正序遍历会导致一直是inf
                # 2. 即使初始化day=1的状态，也会导致某些天会复用一些工作，导致结果不正确
                for x in range(i - 1, j - 2, -1):
                    maxDifficulty = max(maxDifficulty, jobDifficulty[x])
                    dp[i][j] = min(dp[i][j], dp[x][j - 1] + maxDifficulty)
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    # res = solution.minDifficulty([186,398,479,206,885,423,805,112,925,656,16,932,740,292,671,360], 4)
    res = solution.minDifficulty([6, 5, 4, 3, 2, 1], 2)
    print(res)
