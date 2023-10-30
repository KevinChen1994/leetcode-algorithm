from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # 初始状态是不进行分割，每个位置进行累加
        dp = [sum(arr[:i]) for i in range(len(arr) + 1)]
        for i in range(1, len(arr) + 1):
            # 定义在当前的区间内的最大值，先设置为最小值
            max_num = float('-inf')
            for j in range(1, k + 1):
                # 这样限定就决定了我们是从后往前进行划分区间，结束位置就是i，区间为[i-j,i]
                if i - j >= 0:
                    # 因为我们是逐步进行扩大区间，所以每次对比当前区间的最大值
                    max_num = max(max_num, arr[i - j])
                    # 当前位置的最大和为dp[i]（即不进行划分区间，或者之前计算的最大值），或者上一个区间的和加上当前区间最大值的累加和
                    dp[i] = max(dp[i], dp[i - j] + max_num * j)
        return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    res = solution.maxSumAfterPartitioning([1,15,7,9,2,5,10], 3)
    print(res)