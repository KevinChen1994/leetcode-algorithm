# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/5 22:45
from typing import List
import collections

'''
solution: 使用dp字典存储数，key为arr中的数字，value为等差数列的个数。
'''
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = collections.defaultdict(int)
        ans = 0
        for num in arr:
            dp[num] = dp[num - difference] + 1
            ans = max(ans, dp[num])
        return ans


if __name__ == '__main__':
    solution = Solution()
    # arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    # difference = -2
    arr = [3, 4, -3, -2, -4]
    difference = -5
    print(solution.longestSubsequence(arr, difference))
