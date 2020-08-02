# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/23 14:19
'''
solution: 用max_position来记录当前可以跳到的最远位置，如果max_position大于序列长度可以直接返回True.在遍历过程中更新能跳到的最远位置，为当前位置加上当前值。如果当前位置小于可以跳到的最远位置，说明怎么也跳不到这里，需要返回False。
'''
class Solution:
    def canJump(self, nums):
        max_position = 0
        for i in range(len(nums)):
            if max_position >= len(nums):
                return True
            if i > max_position:
                return False
            else:
                max_position = max(max_position, nums[i] + i)
        return True


if __name__ == '__main__':
    solution = Solution()
    # nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    print(solution.canJump(nums))
