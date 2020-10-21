# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/19 23:20
'''
solution1: 记dp[i][j]为i个色子得到j的次数，那么dp[i][j]就可以通过减少一个色子，然后通过最后一个色子的点数来计算。
例如：dp[2][4]，可以记为dp[1][1]+dp[1][3]+dp[1][2]，刚开始这样有点不好理解，后来终于想明白了：
dp[1][1]其实代表了当前已经扔了一个色子是1了，那么还需要扔一个3，同理dp[1][3]代表当前扔了一个色子是3了，还需要扔一个1。
这里需要注意dp数组定义的时候需要多增加一行，因为索引从1开始。
solution2: 由于每个状态只与前一个状态有关，所以没必要使用二维数组保存数据，将dp数据变成一维数组。
'''


class Solution:
    def twoSum_1(self, n: int):
        dp = [[0] * 7 ** n for _ in range(n + 1)]
        for i in range(1, 7):
            dp[1][i] = 1
        for i in range(2, n + 1):
            for j in range(i, 6 * i + 1):
                for cur in range(1, 7):
                    if j - cur <= 0:
                        break
                    dp[i][j] += dp[i - 1][j - cur]
        res = []
        for i in range(n, 6 * n + 1):
            res.append(dp[n][i] / 6 ** n)
        return res

    def twoSum_2(self, n):
        # 索引0不取，从1开始
        dp = [0] * (6 * n + 1)
        for i in range(1, 7):
            dp[i] = 1
        for i in range(2, n + 1):
            # 倒序进行计算，最大为6*n,最小是色子个数
            for j in range(6 * n, i - 1, -1):
                # 每次扔都要从0开始计算
                dp[j] = 0
                for cur in range(1, 7):
                    # 如果当前点数减去这次扔的点数小于最小的点数，那么停止扔色子
                    if j - cur < i - 1:
                        break
                    dp[j] += dp[j - cur]
        res = []
        for i in range(n, 6 * n + 1):
            res.append(dp[i] / 6 ** n)
        return res


if __name__ == '__main__':
    solution = Solution()
    n = 1
    print(solution.twoSum_2(n))
