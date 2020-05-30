# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/13 22:20
'''
solution: 动态规划。定义动态转移矩阵ans，矩阵转移方程为ans[n] = max(ans[n-1], ans[n-2]+nums[n-1]). ans[n-1]的意思就是在n的上一个位置的偷盗全部金额，
ans[n-2]+nums[n-1]的意思就是在n当前这个位置进行偷盗，所以需要在ans[n-2](n的前两个位置偷盗的全部金额)在加上nums[n-1]的值(nums[n-1]代表当前值，因为ans比nums要多一位)。
所以，整个流程就是隔一位才会进行偷盗，最终判断ans的最后一位就是最大的偷盗金额。
参考 https://leetcode-cn.com/problems/house-robber/solution/dong-tai-gui-hua-jie-ti-si-bu-zou-xiang-jie-cjavap/
这篇题解的主要思想就是分解子问题：在n这个位置有两种偷盗方案，一个是偷盗n-1这个位置，也就是n前一个位置的房子，计算公式为ans[n-1]，就是n-1之前的盗窃最大金额，
另一个是偷盗n这个位置，也就是当前的房子，计算公式为ans[n-2]+nums[n-1]，就是n前两个房子之前最大的盗窃金额加上当前房子的金额。
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
