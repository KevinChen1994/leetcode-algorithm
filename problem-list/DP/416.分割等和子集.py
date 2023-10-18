from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        half_nums = nums_sum // 2
        # dp[i]记录当前数字能否被nums中的数字凑出来（数字只用一次）
        dp = [False] * (half_nums + 1)
        dp[0] = True
        # 因为数字只能用一次，所以先循环nums
        for num in nums:
            # 从序列和开始遍历，一直到当前数字，目的是判断当前位置能否被凑出来
            for i in range(half_nums, num - 1, -1):
                # 如果当前位置被凑出来则为True，否则为False
                # 这里需要用到or是因为，dp每个位置都会遍历很多次，因为当前的num不同，所以dp[i]的值也会有变化
                # 那当dp[i]为True的时候需要记录下来，否则后续可能会被覆盖，那使用or就保证了只有dp[i]为True过，就不会再变
                dp[i] = dp[i] or dp[i - num]
        return dp[half_nums]

if __name__ == '__main__':
    solution = Solution()
    # res = solution.canPartition([1,5,11,5])
    res = solution.canPartition([2,2,1,1])
    print(res)