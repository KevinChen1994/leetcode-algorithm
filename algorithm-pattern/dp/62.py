# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/23 10:35
'''
solution: 在第一行的第一列移动时，路径的个数并不会变化，到了其他的行列中，每个坐标的路径计算方法为上边的路径和加上左边的路径和。
注意一点初始化方法：dp = [[0] * n] * m 与 dp = [[0 for i in range(n)] for j in range(m)]
第一种方法是得到的结果每一列中所有的值地址都是一样的，所以在赋值时，会同时修改整个列；第二种方法不会发生这种情况，尽量用第二种方法。
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    m = 3
    n = 3
    print(solution.uniquePaths(m, n))
