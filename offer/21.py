# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/27 22:54

class Solution:
    def exchange(self, nums):
        right = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                nums[i], nums[right] = nums[right], nums[i]
                right += 1
        return nums


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 8, 4, 2, 2, 3, 5, 90, 2, 1]
    print(solution.exchange(nums))
