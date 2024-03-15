from typing import List
'''
使用dp的思路想了半天，也没想清楚转移矩阵是什么，只想到了每次组成三角形都是使用相邻的两个点跟另外的一个点去结合，但是最终条件是什么没有想清楚。
后来又想到这种思路不对，因为有可能是内部的三角形，并没有使用到相邻的两个点。
'''

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        def dfs(i, j):
            if i + 1 == j:
                return 0
            return min(dfs(i, k) + dfs(k, j) + values[i] * values[k] * values[j] for k in range(i + 1, j))
        return dfs(0, len(values) - 1)
    
    def minScoreTriangulation2(self, values: List[int]) -> int:
        '''
        动态规划算法，dp[i][j]表示使用i到j索引能组成的最小数字。
        动态转移矩阵需要计算到i和j之间的数，所以需要i倒序，j正序
        '''
        dp = [[0] * len(values) for _ in range(len(values))]

        for i in range(len(values) - 3, -1, -1):
            for j in range(i + 2, len(values)):
                dp[i][j] = min(dp[i][k] + dp[k][j] + values[i] * values[k] * values[j] for k in range(i + 1, j))
        return dp[0][-1]


if __name__ == '__main__':
    solution = Solution()
    values = [3,7,4,5]
    values = [1,3,1,4,1,5]
    res = solution.minScoreTriangulation2(values)
    print(res)
