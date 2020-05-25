# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/25 17:41
'''
solution1: 超时
solution2: 前缀和。超时。计算每一个位置前的和，以索引为为Key。然后固定左边，右边递增，用前缀和相减。
solution3:
'''


class Solution:
    def subarraySum_1(self, nums, k):
        ans = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    ans += 1

        return ans

    def subarraySum_2(self, nums, k):
        ans = 0
        pre_sum = {0: 0}
        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if pre_sum[j + 1] - pre_sum[i] == k:
                    ans += 1
        return ans

    def subarraySum_3(self, nums, k):
        from collections import defaultdict
        ans = 0
        pre_sum_freq = defaultdict(int)
        pre_sum_freq[0] = 1
        pre_sum = 0
        for num in nums:
            pre_sum += num
            if pre_sum - k in pre_sum_freq:
                ans += pre_sum_freq[pre_sum - k]
            pre_sum_freq[pre_sum] += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 1]
    k = 2
    nums = [28, 54, 7, -70, 22, 65, -6]
    k = 100
    # nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # k = 0
    print(solution.subarraySum_3(nums, k))
