# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/24 17:44
'''
solution1: 传统的dp思路，每一个位置的最长上升序列取决于他的上一个位置，依次类推，把问题分割成小问题去解决。定义dp数组，初始值为1，
遍历到i位置时，需要将i之前的全部数字看一遍，记录下最长的上升子序列，更新到dp数组中。
solution2: 使用tail数组记录下最长上升子序列，规则为，在遍历数组过程中，如果当前元素大于tail最后一个元素，直接放到tail数组最后，
如果小于tail最后一个元素，那么通过二分查找找到第一个比当前元素大于或者等于的数，进行替换，这样就得到了一个结尾更小的相同长度的上升子序列
参考https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
'''
class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)


class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        tail = [nums[0]]
        for i in range(1, len(nums)):
            # 如果当前元素比tail最后一个元素大，直接放到tail数组中
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue
            # 如果当前元素比tail数组最后一个元素小，那么通过二分查找进行查找
            # 找到第 1 个大于等于 nums[i] 的元素，尝试让那个元素更小，注意是第一个大于等于num[i]的元素！！！
            left = 0
            right = len(tail) - 1
            while left < right:
                mid = (left + right) // 2
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = nums[i]
        return len(tail)


if __name__ == '__main__':
    solution = Solution()
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    nums = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
    print(solution.lengthOfLIS(nums))
