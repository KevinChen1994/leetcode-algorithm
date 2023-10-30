from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        temp = target + sum(nums)
        if temp < 0 or sum(nums) < target or temp % 2 != 0:
            return 0
        temp //= 2
        dp = [0] * (temp + 1)
        dp[0] = 1
        for num in nums:
            for i in range(temp, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[-1]
    
if __name__ == '__main__':
    solution = Solution()
    res = solution.findTargetSumWays([1, 1, 1], 1)
    print(res)
