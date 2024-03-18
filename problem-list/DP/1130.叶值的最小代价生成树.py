from typing import List
'''
太难了，没做出来
'''

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float('inf')] * n for _ in range(n)]
        mval = [[0] * n for _ in range(n)]

        for j in range(n):
            mval[j][j] = arr[j]
            dp[j][j] = 0
            for i in range(j - 1, -1, -1):
                mval[i][j] = max(arr[i], mval[i + 1][j])
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + mval[i][k] * mval[k + 1][j])

        return dp[0][-1]

    
if __name__ == '__main__':
    solution = Solution()
    arr = [6,2,4]
    res = solution.mctFromLeafValues(arr)
    print(res)