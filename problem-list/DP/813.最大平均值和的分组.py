from typing import List
from itertools import accumulate
'''
定义dp[i][j]为i个数字，在分隔为j个数组时最大的平均和，当分割数组为1时，平均和也就是整个数组的平均值
当分割数组j>1时，假设存在一个分割点x，使得nums[x:n+1]的平均值，加上之前的平均值最大
之前的平均值已经通过动态规划计算出来了
'''


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        # dp[i][j]为i个数字，在分隔为j个数组时最大的平均和
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        sums = [0]
        for i in range(1, n + 1):
            # sums[i]用来记录从0到i的累加和
            sums.append(sum(nums[:i]))
            # 当分割数组为1时，也就是不切分的平均值
            dp[i][1] = sum(nums[:i]) / i
        for j in range(2, k + 1):
            for i in range(j, n + 1):
                # x用来记录当前数组nums[: i + 1]中，以x为下标作为分割
                for x in range(j - 1, i):
                    # 转移矩阵是，减少一个分割，并找到一个新的分割点，使减少一个分割的平均和加上新的分割数组平均值大于原始的平均和
                    dp[i][j] = max(dp[i][j], dp[x][j - 1] + (sums[i] - sums[x]) / (i - x))

        return dp[n][k]
    
    # 因为dp[i][j]的状态都是来源于dp[i][j - 1],所以可以在dp中去掉j，但是遍历的时候，n要倒序遍历
    def largestSumOfAverages2(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = [0] * (n + 1)
        sums = [0]
        for i in range(1, n + 1):
            sums.append(sum(nums[:i]))
            dp[i] = sum(nums[:i]) / i
        for j in range(2, k + 1):
            for i in range(n, j - 1, -1):
                for x in range(j - 1, i):
                    dp[i] = max(dp[i], dp[x] + (sums[i] - sums[x]) / (i - x))
        return dp[-1]






if __name__ == '__main__':
    solution = Solution()
    res = solution.largestSumOfAverages2([9,1,2,3,9], 3)
    print(res)