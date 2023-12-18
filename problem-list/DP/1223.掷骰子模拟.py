from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 6 for _ in range(n + 1)]
        sums = [0] * (n + 1)

        # 因为rollMax的值总是大于1的，所以第一轮投掷中，每个数字都可以出现。
        # sums记录了当前投掷的次数i中，出现的数字排列的总和
        # dp[i][j]记录了i轮，以j结尾的排列总数量
        for j in range(6):
            sums[1] += 1
            dp[1][j] = 1
        
        for i in range(2, n + 1):
            for j in range(6):
                # k用来确定决定了在当前轮次中能够投掷j的最早位置，如果当前数字已经是无效的了，那么需要剔除掉k以后当前数字出现的组合
                k = i - rollMax[j]
                # 如果k<=1，说明当前的点数还能出现，那么对后续没有影响，invalid值为0。
                # 如果k>1，说明当前点数能出现的次数已经用完了，后续不能出现该点数。
                # sums[k - 1]记录了k轮时总的排列数量，
                # dp[k - 1][j]记录了k轮以j结尾的排列总数据量
                # sums[k - 1] - dp[k - 1][j]表示了k轮时，不以j结尾的排列总数量
                invalid = max(k, 0) if k <= 1 else sums[k - 1] - dp[k - 1][j]
                # 当前轮中以j结尾的排列总数量等于，上一轮中排列总数量减去无效的排列数量
                dp[i][j] = (sums[i - 1] - invalid) % MOD
                # 计算sums[i]的值
                sums[i] = (sums[i] + dp[i][j]) % MOD
        return sums[-1]
    
if __name__ == '__main__':
    solution = Solution()
    # res = solution.dieSimulator(2, [1,1,2,2,2,3])
    res = solution.dieSimulator(3, [1,1,1,2,2,3])
    print(res)
