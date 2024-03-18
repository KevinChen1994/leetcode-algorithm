from typing import List

'''
好难想，反正我没做出来...
'''

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]
        @cache    
        def dfs(i, m):
            if i + m * 2 >= n:
                return piles[i]
            return piles[i] - min(dfs(i + x, max(x, m)) for x in range(1, m * 2 + 1))
        return dfs(0, 1)
    
    def stoneGameII2(self, piles: List[int]) -> int:
        s, n = 0, len(piles)
        dp = [[0] * (n + 1) for _ in range(n)]

        for i in range(n - 1, -1, -1):
            # 后缀和
            s += piles[i]
            for m in range(1, i // 2 + 2):
                if i + m * 2 >= n:
                    dp[i][m] = s
                else:
                    dp[i][m] = s - min(dp[i + x][max(m, x)] for x in range(1, m * 2 + 1))
        return dp[0][1]


if __name__ == '__main__':
    solution = Solution()
    piles = [2,7,9,4,4]
    res = solution.stoneGameII2(piles)
    print(res)