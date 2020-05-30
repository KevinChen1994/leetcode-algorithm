# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/10 22:24
# software: PyCharm
'''
思路：在第一行与第一列，不同路径都为1，因为在一行或者一列，只能直着走，所以只有一种路径，
m,n所在的点的不同路径等于(m-1,n)+(m,n-1)的全部不同路径，即dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
不同路径矩阵为下图所示：
1， 1， 1， 1， 1， 1， 1
1， 2， 3， 4， 5， 6， 7
1， 3， 6，10，15，21，28

'''
class Solution:
    # DP
    def uniquePaths(self, m, n):
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    m = 7
    n = 3
    print(solution.uniquePaths(m, n))
