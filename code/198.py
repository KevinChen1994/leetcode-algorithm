# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/13 22:20
'''
solution: 动态规划。定义动态转移矩阵ans，矩阵转移方程为ans[n] = max(ans[n-1], ans[n-2]+nums[n-1]). ans[n-1]的意思就是在n-1这个位置不偷，
ans[n-2]+nums[n-1]的意思就是在n-1这个位置偷，所以需要在ans[n-2]在加上nums[n-1]的值。
'''
class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 0:
            return 0
        ans = [0] * (len(nums) + 1)
        ans[1] = nums[0]
        for i in range(2, len(nums) + 1):
            ans[i] = max(ans[i - 1], ans[i - 2] + nums[i - 1])
        return ans[-1]


if __name__ == '__main__':
    solution = Solution()
    nums = [9, 1, 1, 9, 1, 8]
    nums = [2, 7, 9, 3, 1]
    print(solution.rob(nums))
