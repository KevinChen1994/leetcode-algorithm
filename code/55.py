# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/8 09:57
# software: PyCharm
'''
solution1 每次记录可以跳跃的最大位置，如果遍历过程中，当前位置大于可以跳跃的最大位置，那么就是失败。
'''
class Solution:
    def canJump(self, nums):
        k = 0
        for i in range(len(nums)):
            if i > k:
                return False
            else:
                k = max(k, i + nums[i])

        return True


if __name__ == '__main__':
    solution = Solution()
    # nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    print(solution.canJump(nums))
