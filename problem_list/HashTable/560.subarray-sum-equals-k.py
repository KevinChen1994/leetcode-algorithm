# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/11 16:33
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        ans = 0
        pre_sum = 0
        pre_sum_dict = defaultdict(int)
        pre_sum_dict[0] = 1
        for num in nums:
            pre_sum += num
            ans += pre_sum_dict[pre_sum - k]
            pre_sum_dict[pre_sum] += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, -1, 1]
    k = 1
    nums = [1, 2, 3]
    k = 3
    print(solution.subarraySum(nums, k))
