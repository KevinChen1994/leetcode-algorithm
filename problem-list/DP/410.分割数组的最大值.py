from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        sums = [sum(nums[:i]) for i in range(1, n + 1)]
        sums.insert(0, 0)
        for i in range(1, n + 1):
            dp[1][i] = sums[i]
        for i in range(2, k + 1):
            for j in range(i, n + 1):
                for x in range(j):
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][x], sums[j] - sums[x]))

        return dp[-1][-1]
    

if __name__ == '__main__':
    solution = Solution()
    res = solution.splitArray([7,2,5,10,8], 2)
    print(res)