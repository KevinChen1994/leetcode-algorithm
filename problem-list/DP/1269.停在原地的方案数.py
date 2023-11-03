

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        # 当arrLen大于steps时，是不可能回到原点的，因为arrLen为长度，并且索引从0开始，那么最大索引为arrLen - 1
        # 所以要取steps和arrLen - 1之间最小的，
        arrLen = min(steps, arrLen - 1)
        # dp[i][j]为i步之后，位于j点的方案数，i为剩余步数，j为当前位置
        dp = [[0] * (arrLen + 1) for _ in range(steps + 1)]
        dp[0][0] = 1
        for i in range(1, steps + 1):
            for j in range(arrLen + 1):
                # 我们要考虑dp[i][j]有几种方案，那么就是由哪些方向可以到达dp[i][j]，
                # 可以由3种方案，分别是原地不动、从右边过来、从左边过来。
                # 原地不动，即位置不变，steps - 1
                # 从右边过来，即位置 + 1，steps - 1
                # 从左边过来，即位置 - 1， steps - 1

                # 因为在任意位置都可以原地不动，方案数可以为dp[i-1][j]的方案数相加
                dp[i][j] = dp[i - 1][j]
                # 当前位置右侧没有到头时，可以认为从右侧往左走一步，那么到当前位置的方案数就可以由右侧的方案数相加
                if j + 1 <= arrLen:
                    dp[i][j] += dp[i - 1][j + 1]
                # 当前位置左侧还有位置时，可以认为从左侧往右走一步，那么到当前位置的方案数就可以由左侧的方案数相加
                if j - 1 >= 0:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[steps][0] % MOD
    
    def numWays2(self, steps: int, arrLen: int) -> int:
        # 从上边的转移矩阵可以看出来dp[i]都是由dp[i - 1]转移过来的，所以我们可以优化这部分空间
        MOD = 10 ** 9 + 7
        arrLen = min(steps, arrLen - 1)
        dp = [0] * (arrLen + 1)
        dp[0] = 1
        for i in range(1, steps + 1):
            # 使用临时数据来记录当前steps下的方案数，最后在同步到dp数组中
            temp = [0] * (arrLen + 1)
            for j in range(arrLen + 1):
                temp[j] += dp[j]
                if j + 1 <= arrLen:
                    temp[j] += dp[j + 1]
                if j - 1 >= 0:
                    temp[j] += dp[j - 1]
            dp = temp
        return dp[0] % MOD



if __name__ == '__main__':
    solution = Solution()
    res = solution.numWays2(4, 2)
    print(res)
