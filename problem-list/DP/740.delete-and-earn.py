# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/23 17:40
from typing import List
'''
solution: 这道题可以转换为198打家劫舍，通过要求发现，如果任意取一个数，那么数组中所有的这个数都可以取到，
而挨着这个数的左右两边的数都不可以取到，打家劫舍也是这个要求，相邻的房子不能同时偷。
那么需要将数组进行转换，首先求出最大值和最小值，创建一个新数组，新数组的长度是最大值-最小值+1，然后将原数组中的值一一填到新数组中，
相同的数字需要累加进固定的位置，如果某个位置没有值，那么就设置为0。
举个例子：nums=[2,2,4,4,5] --> new_nums=[2+2,0,4+4,5] = [4,0,8,5]。这里的0代表的就是3，因为原数组没有所以设置为0。
'''

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_num = max(nums)
        min_num = min(nums)
        new_nums = [0] * (max_num - min_num + 1)
        for num in nums:
            new_nums[num - min_num] += num
        return self.rob(new_nums)

    def rob(self, nums):
        n = len(nums)
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = max((dp[i - 2] if i > 1 else 0) + nums[i], dp[i - 1] if i > 0 else 0)
        return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    nums = [2, 2, 3, 3, 3, 4]
    nums = [3, 4, 2]
    print(solution.deleteAndEarn(nums))