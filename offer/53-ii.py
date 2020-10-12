# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/12 16:50
'''
solution: 二分查找，如果中间的数等于他的索引，那么往右找；如果不等于索引，那么往左找。
需要处理的比较难的是，前边连续，缺少最后一个，例如[0]，缺少1，那么这种情况就是left = mid + 1即可解决。
'''
class Solution:
    def missingNumber(self, nums) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left


solution = Solution()
nums = [0]
print(solution.missingNumber(nums))
